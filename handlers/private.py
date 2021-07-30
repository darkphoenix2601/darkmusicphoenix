from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""I am **{bn}** !!
I let you play music in your group's voice chat 😉
Currently I am under a private vc music player ⏩
To add me take permission from [Owner](https://t.me/backup_pista123)
Dm him directly no tension ❤️
The commands I currently support are:
⚜️ /play - __Plays the replied audio file or YouTube video through link.__
⚜️ /pause - __Pause Voice Chat Music.__
⚜️ /resume - __Resume Voice Chat Music.__
⚜️ /skip - __Skips the current Music Playing In Voice Chat.__
⚜️ /stop - __Clears The Queue as well as ends Voice Chat Music.__
⚜️ /song (song name) - __To search song and send song directly.__
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group 💬", url="https://t.me/RIDERIANS"
                    ),
                    InlineKeyboardButton(
                        "Channel 📣", url="https://t.me/riderians"
                    ),
                    InlineKeyboardButton(
                        "Owner 👑", url="https://t.me/backup_pista123"
                    )
                ]
            ]
        )
    )
