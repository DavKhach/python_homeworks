from users.user import User
from messages.message import TextMessage, MultimediaMessage


def main():
    alice = User("Alice", "alice@example.com")
    bob = User("Bob", "bob@example.com")

    conversation = alice.create_conversation(bob)

    text_message = TextMessage(sender=alice, conversation=conversation, content="Hello Bob")
    alice.send_message(text_message, conversation)

    multimedia_message = MultimediaMessage(sender=bob, conversation=conversation, file_path="/images/photo.jpg", media_type="Image")
    bob.send_message(multimedia_message, conversation)

    print("\n--- Conversation History ---")
    for message in conversation.get_messages():
        message.display_content()

if __name__ == "__main__":
    main()
