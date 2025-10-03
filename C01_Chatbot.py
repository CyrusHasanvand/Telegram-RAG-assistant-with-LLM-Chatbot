#
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from requests.exceptions import Timeout, RequestException
import requests
import json

from ConnectMySQL import save_chat

TELEGRAM_TOKEN = "1023456789:AWFETzeOSSkGyskv1anq5QvTKibQsz-G5xi"

system_prompt = """
You are an expert AI assistant.
Answer concisely but fully.
Limit each response to 100 words if possible.
Do not use stars (*,**) in your response.
"""
chat_history={}
def query_ollama(context_prompt: str):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3.1",
        "prompt": context_prompt,
        "stream": True,   # 👈 disable streaming
        "options": {
            "num_predict": 450,   # 👈 limit tokens (shorter = faster)
            "temperature": 0.3    # 👈 lower randomness, more deterministic
        }
    }
    try:
        resp = requests.post(url, json=payload, stream=True, timeout=150)
        resp.raise_for_status()

        response = ""
        for line in resp.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                if "response" in data:
                    response += data["response"]

        return response.strip() if response else "⚠️ No response from model."

    except Timeout:
        # Custom message for timeout
        return "⚠️ The server is busy. Please try your question a few minutes later."
    except RequestException as e:
        # Any other request-related error
        return f"⚠️ Error: {e}"
    except Exception as e:
        return f"⚠️ Unexpected error: {e}"



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.message.from_user.first_name
    await update.message.reply_text(f"Hi {user_first_name}!\nThis is a chatbot designed by Cyrus. How can I help you today?")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_message = update.message.text
    # initialize history
    if user_id not in chat_history:
        chat_history[user_id] = []
    # add user message
    chat_history[user_id].append(f"User: {user_message}")
    chat_history[user_id] = chat_history[user_id][-10:]
    # Include system prompt here
    context_prompt = system_prompt + "\n" + "\n".join(chat_history[user_id]) + "\nAI:"
    # query model
    response = query_ollama(context_prompt)
    # add model response to history
    chat_history[user_id].append(f"AI: {response}")

    # save conversation to MySQL
    save_chat(user_id, update.message.from_user.username, user_message, response)

    #user_message = update.message.text
    #response = query_ollama(user_message)
    await update.message.reply_text(response)

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    app.run_polling()

if __name__ == "__main__":
    main()