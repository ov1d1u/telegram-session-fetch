from telethon import TelegramClient
from telethon.sessions import StringSession

TELEGRAM_API_ID = input("Enter your Telegram API ID: ")
TELEGRAM_API_HASH = input("Enter your Telegram API HASH: ")

print("")

client = TelegramClient(StringSession(), int(TELEGRAM_API_ID), TELEGRAM_API_HASH)
client.start()

session = client.session.save()
print("Here is your Telegram String Session:\n\n" + session)
