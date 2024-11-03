import pyrogram
from utils.secretsCred import api_id, api_hash, bot_token, chat_id

plugins = dict(root="plugins")
app = pyrogram.Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token,
    plugins=plugins
)

async def send_message(message):
    global app
    await app.send_message(chat_id, message,disable_web_page_preview=False)