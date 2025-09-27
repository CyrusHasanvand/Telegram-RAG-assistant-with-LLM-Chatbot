# Telegram RAG assistant
Assume that you have a product and want to hire an AI to communicate with users through Telegram on behalf of your team as an employee at your company, in which an AI agent responds to users automatically based on the retrieved information or by mixing information of both the AI's pre-knowledge itself and your data. Therefore, having an intelligent AI would be the most important thing to provide for your customers. They can communicate with your AI agent to learn more about your company's aim, products, and related information from AI suggestions to let users engage beneficially with your team and items. More importantly, this communication is available everywhere and at any time of the day.

## Why Telegram?
In this project, I have utilized Telegram for this command because of its capabilities, diversity, and security. You can use an alternative based on what you prefer. However, you need a chat environment, which could be designed on your own website.

## Framework setups
To develop this project, we need to handle three main subjects, including ```i)``` Chatting environment (which is Telegram here); ```ii)``` LLM model in the backend (which is local ```llama3.1``` in this project); and ```iii)``` a database to save the logs and chats (which is ```MySQL``` in the current mission).

### i) Creating Telegram chatbot
We need an API to connect different models. Therefore, we have to address a ```token``` number in Telegram to connect the chats with our backend LLM model through an ```HTTP API```.
to use the Telegram  
To create your own chatbot, you need to search ```BotFather``` in Telegram, which show you  






![](Images/Im_01.png)
