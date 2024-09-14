from datetime import datetime
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod


if TYPE_CHECKING:
    from users.user import User
    from conversations.conversation import Conversation

class Message(ABC):
    def __init__(self, sender: "User", conversation: "Conversation"):
        self.sender = sender
        self.conversation = conversation
        self.timestamp = datetime.now()

    @abstractmethod
    def display_content(self) -> None:
        ...

    @abstractmethod
    def get_message_type(self) -> str:
        ...


class TextMessage(Message):
    def __init__(self, sender: "User", conversation: "Conversation", content: str):
        super().__init__(sender, conversation)
        self.content = content

    def display_content(self) -> None:
        print(f"[{self.timestamp}] {self.sender.name}: {self.content}")

    def get_message_type(self) -> str:
        return "Text"


class MultimediaMessage(Message):
    def __init__(self, sender: "User", conversation: "Conversation", file_path: str, media_type: str):
        super().__init__(sender, conversation)
        self.file_path = file_path
        self.media_type = media_type

    def display_content(self) -> None:
        print(f"[{self.timestamp}] {self.sender.name} sent a {self.media_type}: {self.file_path}")

    def get_message_type(self) -> str:
        return self.media_type
