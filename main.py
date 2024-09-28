import sys
import pyrogram
from pyro_secrets import api_id, api_hash, bot_token
import threading
from time import sleep
from subito_searcher import scrape
import asyncio
from bot import *

async def main():
    await app.start()

    monitoring_thread = threading.Thread(target=asyncio.run, args=(scrape(),), daemon=True)
    monitoring_thread.start()

    await pyrogram.idle()
    await app.stop()


app.run(main())