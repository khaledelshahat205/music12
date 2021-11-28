#vampre
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
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""**مرحبا بك عزيزي, انا {bn} 🎧
🚨 [
ᯓ˹ 𝐕𝘼𝙈𝘽𝙄𝙍𖣥⃟⃟⃟⃟⃟🇵🇸فمـبــيرـ‌）⛧](https://t.me/XxlllllllllllllllllllllllllllxX)  
⌁ ⁞  بوت تشغيل الاغاني  في المكالمه ' الجماعيه وبحث /song +اسم الاغنيه
⌁ ⁞ قم برفع البوت مشرف مع صلاحيه اضافه مستخدمين عبر الرابط
لمعرفه الأوامر اضغط /help 
⌁ ⁞   Developed By [𝐕𝘼𝙈𝘽𝙄𝙍](https://t.me/XxlllllllllllllllllllllllllllxX)!**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "🎧اضافه البوت اللي مجموعتك🎧", url=f"https://t.me/XxlllllllllllllllllllllllllllxX?startgroup=true")
                ],[
                    InlineKeyboardButton(
                         "Updates", url="https://t.me/elnqyb_sp"
                    ),
                    InlineKeyboardButton(
                        "🔮ⓜⓤⓢⓘⓒ🔮", url=f"https://t.me/XxVPlllllllllxX")
                ],[
                    InlineKeyboardButton(
                        "🚨GROUP🚨", url=f"https://t.me/XxllllllllllllllllllllllllllxX"
                    ),
                    InlineKeyboardButton(
                        "🚨𝐒𝐎𝐔𝐑𝐂𝐄🚨", url=f"https://t.me/XxvprxX ")               
                 ],[
                    InlineKeyboardButton(
                        "ᯓ˹ 𝐕𝘼𝙈𝘽𝙄𝙍𖣥⃟⃟⃟⃟⃟🇵🇸فمـبــيرـ‌）⛧ ", url="https://t.me/XxlllllllllllllllllllllllllllxX"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@XxlllllllllllllllllllllllllllxX"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✔ **البوت قيد التشغيل الان**\n<b>💞 **وقت تشغيل البوت :**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🚨ⒷⒶⓇ🚨", url=f"https://t.me/XxllllllllllllllllllllllllllxX"
                    ),
                    InlineKeyboardButton(
                        "🚨𝐒𝐎𝐔𝐑𝐂𝐄🚨", url=f"https://t.me/XxvprxX "
                    )
                ]
            ]
        )
    )

@Client.on_message(command("help") & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>• الاوامر 

- /play <اسم الأغنية> 
ـ تشغيل الأغنية التي طلبتها. 

- /playlist 
ـ عرض قائمة التشغيل الآن. 

- /song <اسم الاغنيه>
ـ تنزيل الأغاني التي تريدها بسرعة. 

- /search <اسم الاغنيه> 
ـ البحث في اليوتيوب مع التفاصيل. 

- /vsong <اسم الاغنيه>
ـ تنزيل مقاطع الفيديو التي تريدها بسرعة

- /lyric <اسم الاغنيه>
ـ إحضار كلمات الاغنيه. 

• الاوامر الخاصه بِ المشرفين فقط . 
 
- /player  
ـ فتح لوحة إعدادات مشغل الموسيقى

- /pause 
ـ وقف تشغيل الاغنيه الحاليه. 

- /resume
ـ استئناف تشغيل الأغنية. 

- /skip 
ـ التقدم للأغنية التالية

- /end 
ـ إيقاف تشغيل الموسيقى. 

- /musicplayer on 
ـ لتعطيل مشغل الموسيقى في مجموعتك. 

- /musicplayer off 
- لتمكين مشغل الموسيقى في مجموعتك. 

- /userbotjoin 
- دعوة المساعد إلى الدردشه الحاليه 

- /userbotleave 
- إزالة المساعد من الدردشة الحالية. 

- /reload 
- تحديث قائمة الإدارة. 

- /uptime 
- التحقق من وقت تشغيل البوت

- /ping 
- تحقق من حالة البوت 

• الاوامر الخاصه بالمطورين

- /pmpermit on | off  
ـ قفل/فتح الدردشه ف الخاص. 

- /userbotleaveall 
- اطلب من المساعد مغادرة جميع المجموعات

- /gcast 
- عمل إذاعه

• الشات الخاص بالبوت المساعد 

- .yes 
- الموافقة على إرسال رسالة إلى المساعد في الخاص. 

- .no 
- رفض إرسال رسالة إلى المساعد في الخاص.
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🚨ⒷⒶⓇ🚨", url=f"https://t.me/XxllllllllllllllllllllllllllxX"
                    ),
                    InlineKeyboardButton(
                        "🚨𝐒𝐎𝐔𝐑𝐂𝐄🚨", url=f"https://t.me/XxvprxX "
                    )
                ],
                [
                    InlineKeyboardButton(
                        "𝐕𝘼𝙈𝘽𝙄𝙍", url=f"https://t.me/XxlllllllllllllllllllllllllllxX"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["ping", f"ping@XxlllllllllllllllllllllllllllxX"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ᴘɪɴɢɪɴɢ...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "🖱️ `ᴘᴏɴɢ!!`\n"
        f"🚨 `{delta_ping * 1000:.3f} ᴍs`"
    )


@Client.on_message(command(["uptime", f"uptime@XxlllllllllllllllllllllllllllxX"]) & ~filters.edited)
@authorized_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        " ʙᴏᴛ sᴛᴀᴛᴜs:\n"
        f"➤🚨 **ᴜᴘᴛɪᴍᴇ:** `{uptime}`\n"
        f"➤🚨 **sᴛᴀʀᴛ ᴛɪᴍᴇ:** `{START_TIME_ISO}`"
    )
