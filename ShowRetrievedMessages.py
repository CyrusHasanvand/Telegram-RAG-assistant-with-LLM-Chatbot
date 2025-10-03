from RetrieveMySQL import fetch_chats

chats = fetch_chats(2)  #last 10 rows
for chat in chats:
    print(f"[{chat['create_at']}] {chat['username']} -> {chat['message']}")
    print(f"AI: {chat['reply']}")
    print("*******************************************")

