import logging
import importlib

from pyrogram import idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Mitsuri import info, mitsuri, LOG_GROUP_ID
from Mitsuri.plugins import ALL_MODULES

if __name__ == "__main__":
    logging.basicConfig(
        handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
        level=logging.INFO,
        format="%(message)s",
        datefmt="[%X]",
    )
    logging.getLogger("pyrogram").setLevel(logging.INFO)

    failed_modules = []
    loaded_modules = []

    for module in ALL_MODULES:
        try:
            importlib.import_module("Mitsuri.plugins." + module)
            loaded_modules.append(module)
        except Exception as e:
            failed_modules.append((module, e))

    idle()

    if failed_modules:
        message = "**Mitsuri failed to load these modules:**\n\n"
        for module, error in failed_modules:
            message += f"➤ `{module}`: `{error}`\n"
        mitsuri.send_message(LOG_GROUP_ID, message)
    else:
        mitsuri.send_message(
            LOG_GROUP_ID,
            f"**Mitsuri is online!**\nLoaded `{len(loaded_modules)}` plugins successfully."
      )
