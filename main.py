from telethon import TelegramClient

SESSION_FILE = 'eq_alert.session'
TELEGRAM_API_ID = 123456
TELEGRAM_API_HASH = "1234567890abcdef1234567890abcdef"

client = TelegramClient('session_name', TELEGRAM_API_ID, TELEGRAM_API_HASH)
client.start()
