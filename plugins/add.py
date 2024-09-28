from pyrogram import filters, Client
from plugins.utils import filtro
import datetime

@Client.on_message(filters.command("add") & filtro)
async def add(client, message):
    #respond with hello world
    await message.reply_text("Hello World!")
    