import pyrogram
from pyro_secrets import api_id, api_hash, bot_token

plugins = dict(root="plugins")
app = pyrogram.Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token,
    plugins=plugins
)
chat=512312820

async def send_message(message):
    global app
    await app.send_message(chat, message,disable_web_page_preview=False)