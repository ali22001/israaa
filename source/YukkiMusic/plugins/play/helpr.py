import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
     command(["/help", "الاوامر"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/d6168f7dafba83c27d8a6.jpg",
caption=f"""**[᥉ᥱᥣᥣᥴƚ ᥣᥲ️ꪀᘜυᥲ️ᘜᥱ ƚ᥆ ᥣᥱᥲ️ᖇꪀ ꪔ᥆ᖇᥱ](https://t.me/E_16_E)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "عربي 🇪🇬", callback_data="arbic"
                ),
                ],
                [
                    InlineKeyboardButton(
                        "English 🇺🇲", callback_data="english"),
                ],
            ]
        ),
    )


