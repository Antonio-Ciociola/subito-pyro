from pyrogram import filters, Client

# import TextUrl pyrogram.raw.types.TextUrl
from pyrogram.raw.types import TextUrl
from plugins.utils import filtro
import datetime
from database import *
from secretsCred import chat_id
from bot import app


@Client.on_message(filters.command("list") & filtro)
async def list(client, message):
    queries = getQueries()
    msg = ""
    for query in queries:
        msg += f"Id: {query.id}, name: {query.name}, url: {query.url}, minPrice: {query.minPrice}, maxPrice: {query.maxPrice}\n"
    if msg == "":
        msg = "No queries found"
    await message.reply_text(msg)


@Client.on_message(filters.command("add") & filtro)
async def add(client, message):
    help = "Usage: /add name, url, minPrice, maxPrice.\n\nminPrice and maxPrice are optional use None if not set" 
    query = message.text.split(" ", 1)
    if len(query) < 2:
        await message.reply_text(help)
        return
    query = query[1]
    query = query.split(", ")
    if len(query) < 2:
        await message.reply_text(help)
        return

    name = query[0]
    url = query[1]
    if len(query) > 2 and query[2].isnumeric():
        minPrice = query[2]
    else:
        minPrice = None
    if len(query) > 3 and query[3].isnumeric():
        maxPrice = query[3]
    else:
        maxPrice = None
    addQuery(name, url, minPrice, maxPrice)
    await message.reply_text("Query added")


@Client.on_message(filters.command("remove") & filtro)
async def remove(client, message):
    query = message.text.split(" ")
    if len(query) < 2:
        await message.reply_text("Usage: /remove queryId")
        return
    queryId = query[1]
    queryId = int(queryId)
    removeQuery(queryId)
    await message.reply_text("Query removed")
