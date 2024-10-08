from message import Message
from abc import ABC, abstractmethod
from conversations.conversation import Conversation


class MessagingManager(ABC):
    @abstractmethod
    def send_message(self, message: Message) -> None:
        ...

    @abstractmethod
    def receive_message(self, message: Message) -> None:
        ...

    @abstractmethod
    def view_conversation_history(self, conversation: Conversation) -> list[Message]:
        ...
