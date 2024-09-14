from typing import List
from messages.message import Message
from conversations.conversation import Conversation


class User:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.conversations: List[Conversation] = []

    def create_conversation(self, user: 'User') -> Conversation:
        conversation = Conversation([self, user])
        self.conversations.append(conversation)
        user.conversations.append(conversation)
        return conversation

    def send_message(self, message: 'Message', conversation: 'Conversation') -> None:
        if conversation in self.conversations:
            conversation.add_message(message)
        else:
            print("You are not part of this conversation.")

    def receive_message(self, message: 'Message') -> None:
        print(f"New message for {self.name}:")
        message.display_content()

    def manage_settings(self) -> None:
        print(f"Managing settings for {self.name}")

    def get_conversations(self) -> List['Conversation']:
        return self.conversations
