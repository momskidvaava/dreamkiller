import random

import requests
from pyrogram import filters
from pyrogram.types import *
from telethon import Button, events

from dreamkiller import pgram as bot
from dreamkiller import telethn as asst


@bot.on_message(filters.command("wish"))
async def wish(_, m):
    if len(m.command) < 2:
        await m.reply("😉 **Add your wish!**")
        return
    api = requests.get("https://nekos.best/api/v2/happy").json()
    url = api["results"][0]["url"]
    text = m.text.split(None, 1)[1]
    wish_count = random.randint(1, 100)
    wish = f"✨ **Hey! {m.from_user.first_name}!** 🙋‍♀️\n"
    wish += f"✨ **Your wish**: **{text}** 🧚🏻‍♀️"
    wish += f"✨ **Possible to: {wish_count}%**"
    await m.reply_animation(
        url,
        caption=(wish),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❔ What is This", url="https://t.me/StrawHatUpdates/14"
                    )
                ]
            ]
        ),
    )


BUTTON = [[Button.url("❔ What Is This", "https://t.me/StrawHatUpdates/11")]]
HOT = "https://c.tenor.com/XofRuAsQH7EAAAAC/anime-sexy.gif"
SMEXY = "https://telegra.ph/file/3b07b0891fe71e3fb3f3d.mp4"
LEZBIAN = "https://pa1.narvii.com/5853/e40f2e8c88da7d0cf3f33f492aa445bab598c4a5_hq.gif"
BIGBALL = "https://i.gifer.com/8ZUg.gif"
LANG = "https://telegra.ph/file/423414459345bf18310f5.gif"
CUTIE = "https://data.whicdn.com/images/328417923/original.gif"


@asst.on(events.NewMessage(pattern="/horny ?(.*)"))
async def horny(e):
    if not e.is_reply:
        user_id = e.sender.id
        user_name = e.sender.first_name
        mention = f"[{user_name}](tg://user?id={str(user_id)})"
        mm = random.randint(1, 100)
        HORNY = f"**🔥** {mention} **Is** {mm}**% Horny!**"
        await e.reply(HORNY, buttons=BUTTON, file=HOT)
    if e.is_reply:
        replied = await e.get_reply_message()
        id = replied.sender.id
        name = replied.sender.first_name
        mention = f"[{name}](tg://user?id={str(id)})"
        mm = random.randint(1, 100)
        HORNY = f"**🔥** {mention} **Is** {mm}**% Horny!**"
        await e.reply(HORNY, buttons=BUTTON, file=HOT)


@asst.on(events.NewMessage(pattern="/gay ?(.*)"))
async def gay(e):
    if not e.is_reply:
        user_id = e.sender.id
        user_name = e.sender.first_name
        mention = f"[{user_name}](tg://user?id={str(user_id)})"
        mm = random.randint(1, 100)
        GAY = f"**🏳‍🌈** {mention} **Is** {mm}**% Gay!**"
        await e.reply(GAY, buttons=BUTTON, file=SMEXY)
    if e.is_reply:
        replied = await e.get_reply_message()
        id = replied.sender.id
        name = replied.sender.first_name
        mention = f"[{name}](tg://user?id={str(id)})"
        mm = random.randint(1, 100)
        GAY = f"**🏳‍🌈** {mention} **Is** {mm}**% Gay!**"
        await e.reply(GAY, buttons=BUTTON, file=SMEXY)


@asst.on(events.NewMessage(pattern="/lezbian ?(.*)"))
async def lezbian(e):
    if not e.is_reply:
        user_id = e.sender.id
        user_name = e.sender.first_name
        mention = f"[{user_name}](tg://user?id={str(user_id)})"
        mm = random.randint(1, 100)
        FEK = f"**💜** {mention} **Is** {mm}**% Lezbian!**"
        await e.reply(FEK, buttons=BUTTON, file=LEZBIAN)
    if e.is_reply:
        replied = await e.get_reply_message()
        id = replied.sender.id
        name = replied.sender.first_name
        mention = f"[{name}](tg://user?id={str(id)})"
        mm = random.randint(1, 100)
        FEK = f"**💜** {mention} **Is** {mm}**% Lezbian!**"
        await e.reply(FEK, buttons=BUTTON, file=LEZBIAN)


@asst.on(events.NewMessage(pattern="/boobs ?(.*)"))
async def boobs(e):
    if not e.is_reply:
        user_id = e.sender.id
        user_name = e.sender.first_name
        mention = f"[{user_name}](tg://user?id={str(user_id)})"
        mm = random.randint(1, 100)
        BOOBS = f"**🍒** {mention}**'s Boobs Size Is** {mm}**!**"
        await e.reply(BOOBS, buttons=BUTTON, file=BIGBALL)
    if e.is_reply:
        replied = await e.get_reply_message()
        id = replied.sender.id
        name = replied.sender.first_name
        mention = f"[{name}](tg://user?id={str(id)})"
        mm = random.randint(1, 100)
        BOOBS = f"**🍒** {mention}**'s Boobs Size Is** {mm}**!**"
        await e.reply(BOOBS, buttons=BUTTON, file=BIGBALL)


@asst.on(events.NewMessage(pattern="/cock ?(.*)"))
async def cock(e):
    if not e.is_reply:
        user_id = e.sender.id
        user_name = e.sender.first_name
        mention = f"[{user_name}](tg://user?id={str(user_id)})"
        mm = random.randint(1, 100)
        COCK = f"**🍆** {mention}**'s Cock Size Is** {mm}**cm**"
        await e.reply(COCK, buttons=BUTTON, file=LANG)
    if e.is_reply:
        replied = await e.get_reply_message()
        id = replied.sender.id
        name = replied.sender.first_name
        mention = f"[{name}](tg://user?id={str(id)})"
        mm = random.randint(1, 100)
        COCK = f"**🍆** {mention}**'s Cock Size Is** {mm}**cm**"
        await e.reply(COCK, buttons=BUTTON, file=LANG)


@asst.on(events.NewMessage(pattern="/cute ?(.*)"))
async def cute(e):
    if not e.is_reply:
        user_id = e.sender.id
        user_name = e.sender.first_name
        mention = f"[{user_name}](tg://user?id={str(user_id)})"
        mm = random.randint(1, 100)
        CUTE = f"**🍑** {mention} {mm}**% Cute**"
        await e.reply(CUTE, buttons=BUTTON, file=CUTIE)
    if e.is_reply:
        replied = await e.get_reply_message()
        id = replied.sender.id
        name = replied.sender.first_name
        mention = f"[{name}](tg://user?id={str(id)})"
        mm = random.randint(1, 100)
        CUTE = f"**🍑** {mention} {mm}**% Cute**"
        await e.reply(CUTE, buttons=BUTTON, file=CUTIE)


__help__ = """
**What is This (wish):**
You having any kind of 
(wishes) you can using this bot to how possible to your wish!
Example:
❍ /wish I want a new iphone 😜

❔ What is This (howall):
In this Howell show you possibility!
Example:
❍ /horny: reply to someone or it self show how horny!
❍ /cute: reply to someone or it self show how cute!
❍ /boobs: reply to someone or it self show how boobs!
❍ /cock: reply to someone or it self show how cock!
❍ /lezbian: reply to someone or it self show how horny!
❍ /gay: reply to someone or it self show how gay!
"""

__mod_name__ = "Howall"
