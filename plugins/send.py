from database import *
from secretsCred import chat_id
from bot import app

async def newItem(item):
    queryName = getQuery(item.queryId).name
    message = f"{queryName}: [{item.title}]({item.url}), €{item.price}, {item.location}"
    await app.send_message(chat_id, message, disable_web_page_preview=False)
    