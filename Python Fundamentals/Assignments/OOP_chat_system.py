from datetime import datetime
class User:
    def __init__(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id
        
    def send_message(self, text, chatroom):
        message = Message(text, self)
        chatroom.add_message(message)

class Message:
    def __init__(self, message_text, time_sent, sender):
        self.message_text = message_text    
        time_sent = datetime.now()
        self.time_sent =  time_sent
        self.sender = sender
        
    
    def send_message(self):
        print(f"{self.time_sent} {self.user_name} : {self.message_text}")
        
class ChatRoom:
    def __init__(self, chat_id, chat_name):
        self.chat_id = chat_id
        self.chat_name = chat_name 
        chat_history = []
        users = []
    def join(self, user):
        self.users.append(user)
    def leave(self, user):
        self.users.remove(user)
    def add_message(self, message):
        self.chat_history.append(message)
    def display_chat_history(self):
        for message in self.chat_history:
            print(
                f"{message.time_sent} "
                f"{message.sender.user_name}: "
                f"{message.message_text}"
            )