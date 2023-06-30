import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["تنصيب","التنصيب","المصنع"])
    & filters.group
    & ~filters.edited
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/d6168f7dafba83c27d8a6.jpg",
        caption=f"""| سورس ريكو لتنـصـيب الـمـيوزك""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "تنصيب الميوزك", url=f"https://t.me/MU_REBOT"),
                    InlineKeyboardButton(
                        "تنصيب التليثون ♡", url=f"https://t.me/OW_A1BOT"),
                ],
                [
                   InlineKeyboardButton(
                        "Rico 𝖳𝖾𝖺𝖬", url=f"https://t.me/E_16_E"),
                ],       
            ]
        ),
    )