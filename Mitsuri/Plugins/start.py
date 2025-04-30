from pyrogram.types import Message
from Mitsuri import mitsuri, get_command

@mitsuri.on_message(get_command("start"))
async def start_cmd(_, message: Message):
    await message.reply_photo(
        photo="https://graph.org/file/e08bcb0f3b34555cc8dc1.jpg",
        caption=(
            "**Hey, I'm Mitsuri!**\n\n"
            "Your cute and helpful management bot!\n"
            "Use /help to explore all my features!"
        )
    )
