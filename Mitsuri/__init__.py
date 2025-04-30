import time
from typing import Union, List
from functools import reduce

from pyrogram import filters, Client
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

from config import API_ID, API_HASH, MONGO_URL, LOG_GROUP_ID
from Mitsuri.funcs.readable_time import get_readable_time

TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"

try:
    mitsuri = Client(
        "Mitsuri",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=TOKEN
    )
    mitsuri.start()
except Exception as e:
    print(f"[ERROR] Bot failed to start: {e}")
    raise SystemExit

mongo_client = MongoClient(MONGO_URL)
database = mongo_client.mitsuri

info = mitsuri.get_me()
StartTime = time.time()
uptime = get_readable_time((time.time() - StartTime))

def parse_com(com: str, keys: Union[str, List[str]]) -> str:
    if isinstance(keys, str):
        keys = [keys]
    for key in keys:
        try:
            r = com.split(key, 1)[1].lstrip()
            return r
        except IndexError:
            pass
    raise ValueError("Invalid command format")

def get_command(comm: Union[str, List[str]]) -> filters.Filter:
    res = []
    if isinstance(comm, str):
        res.extend([comm, f"{comm}@{info.username}"])
    if isinstance(comm, list):
        for com in comm:
            res.extend([com, f"{com}@{info.username}"])
    return filters.command(
        res,
        prefixes=["/", ".", "!", "mitsuri ", "@mitsuri ", "Mitsuri "]
      )
