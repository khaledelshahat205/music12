from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_NAME as bn
from helpers.filters import other_filters2
from time import time
from datetime import datetime
from helpers.decorators import authorized_users_only
from config import BOT_USERNAME, ASSISTANT_USERNAME

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""**مرحبا, انا {bn} 🎧
اسرع بوت اغاني علي التليجرام فيه كل مميزات بحث عن الاغاني اكتب /song +اسم الاغنيه او بحث +اسم الاغنيه ويسمح لك بتشغيل الموسيقى والفيديو في مجموعات من خلال محادثات الفيديو الجديدة في التلي [ᯓ˹ 𝐕𝘼𝙈𝘽𝙄𝙍𖣥⃟⃟⃟⃟⃟🇵🇸فمـبــيرـ͢）⛧](https://t.me/XxlllllllllllllllllllllllllllxX).
⋆ قم بإضافة البوت اللي مجموعتك لكي تبدا الحفله..🚨**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔮ⓜⓤⓢⓘⓒ🔮", url="https://t.me/XxVPlllllllllxX")
                  ],[
                  InlineKeyboardButton(
                        "𝐕𝘼𝙈𝘽𝙄𝙍𖣥⃟⃟⃟⃟⃟🇵🇸", url="https://t.me/XxlllllllllllllllllllllllllllxX")
                  ],[
                    InlineKeyboardButton(
                       "🚨𝐒𝐎𝐔𝐑𝐂𝐄🚨", url="https://t.me/XxvprxX"
                    ),
                    InlineKeyboardButton(
                        "🚨ⒷⒶⓇ🚨", url="https://t.me/XxllllllllllllllllllllllllllxX"
                    )
                ],[
                    InlineKeyboardButton(
                        "🚨اضف البوت لجروبك🚨",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )
