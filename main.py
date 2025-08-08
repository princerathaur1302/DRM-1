import os
import re
import sys
import m3u8
import json
import time
import pytz
import asyncio
import requests
import subprocess
import urllib
import urllib.parse
import yt_dlp
import tgcrypto
import cloudscraper
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64encode, b64decode
from bs4 import BeautifulSoup
import process as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN, OWNER, CREDIT, AUTH_USERS
from aiohttp import ClientSession
from subprocess import getstatusoutput
from pytube import YouTube
from aiohttp import web
import random
from pyromod import listen
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import aiohttp
import aiofiles
import zipfile
import shutil
import ffmpeg

# Initialize the bot
bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

YT = "[𓊈𒆜Y͎O͎U͎T͎U͎B͎E͎𒆜𓊉](https://youtube.com/@LocalBoyPrince)"
ALL = "[♛A͓̽L͓̽L͓̽ B͓̽A͓̽T͓̽C͓̽H͓̽♛](https://t.me/addlist/Yfez5bB2FiljMzE1)"


# Inline keyboard for start command
BUTTONSCONTACT = InlineKeyboardMarkup([[InlineKeyboardButton(text="📞 Contact", url="http://t.me/contact_262524_bot")]])
keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="📞 Contact", url="http://t.me/contact_262524_bot"),
        ],
    ]
)


@bot.on_message(filters.command("adduser") & filters.private)
async def add_auth_user(client: Client, message: Message):
    if message.chat.id != OWNER:
        return await message.reply_text("You are not authorized to use this command.")

    try:
        new_user_id = int(message.command[1])
        if new_user_id in AUTH_USERS:
            await message.reply_text("User ID is already authorized.")
        else:
            AUTH_USERS.append(new_user_id)
            await message.reply_text(f"User ID {new_user_id} added to authorized users.")
    except (IndexError, ValueError):
        await message.reply_text("Please provide a valid user ID.")

@bot.on_message(filters.command("userlist") & filters.private)
async def list_auth_users(client: Client, message: Message):
    if message.chat.id != OWNER:
        return await message.reply_text("You are not authorized to use this command.")

    user_list = '\n'.join(map(str, AUTH_USERS))
    await message.reply_text(f"<blockquote>Authorized Users:</blockquote>\n{user_list}")

@bot.on_message(filters.command("removeuser") & filters.private)
async def remove_auth_user(client: Client, message: Message):
    if message.chat.id != OWNER:
        return await message.reply_text("You are not authorized to use this command.")

    try:
        user_id_to_remove = int(message.command[1])
        if user_id_to_remove not in AUTH_USERS:
            await message.reply_text("User ID is not in the authorized users list.")
        else:
            AUTH_USERS.remove(user_id_to_remove)
            await message.reply_text(f"User ID {user_id_to_remove} removed from authorized users.")
    except (IndexError, ValueError):
        await message.reply_text("Please provide a valid user ID.")




@bot.on_message(filters.command(["upgrade"]))
async def id_command(client, message: Message):
    chat_id = message.chat.id
    await message.reply_text(
        f" 🎉 Welcome {message.from_user.first_name} to DRM Bot! 🎉\n\n"
           f"You can have access to download all Non-DRM+AES Encrypted URLs 🔐 including\n\n"
           f"Use Command : /help to get started 🌟\n\n"
           f"• 🧑‍🏫 Ph*j*CsW*llah DRM\n"
           f"• 🎓 All Non DRM+AES Encrypted URLs\n"
           f"• 🎓 MPD URLs if the key is known (e.g., Mpd_url?key=key XX:XX)\n\n"
           f"<blockquote>💵 Monthly Plan: ₹100</blockquote>\n\n"
           f"If you want to buy membership of the bot, feel free to contact the Bot Admin.\n", disable_web_page_preview=True, reply_markup=BUTTONSCONTACT
    )  



@bot.on_message(filters.command(["stop"]) )
async def restart_handler(_, m):
    if m.chat.id not in AUTH_USERS:
        print(f"User ID not in AUTH_USERS", m.chat.id)
        await bot.send_message(
            m.chat.id, 
            f"<blockquote>__**Oopss! You are not a Premium member**__\n"
            f"__**PLEASE /upgrade YOUR PLAN**__\n"
            f"__**Send me your user id for authorization**__\n"
            f"__**Your User id** __- `{m.chat.id}`</blockquote>\n\n"
        )
    else:
        await m.reply_text("🚦**STOPPED**🚦", True)
        os.execl(sys.executable, sys.executable, *sys.argv)


@bot.on_message(filters.command("start"))
async def start(bot, m: Message):
    user = await bot.get_me()
    mention = user.mention
    start_message = await bot.send_message(
        m.chat.id,
        f"🌟 Welcome {m.from_user.first_name}! 🌟\n\n"
    )

    await asyncio.sleep(1)
    await start_message.edit_text(
        f"🌟 Welcome {m.from_user.first_name}! 🌟\n\n" +
        f"Initializing Uploader bot... 🤖\n\n"
        f"Progress: [⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️] 0%\n\n"
    )

    await asyncio.sleep(1)
    await start_message.edit_text(
        f"🌟 Welcome {m.from_user.first_name}! 🌟\n\n" +
        f"Loading features... ⏳\n\n"
        f"Progress: [🟥🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️] 25%\n\n"
    )

    await asyncio.sleep(1)
    await start_message.edit_text(
        f"🌟 Welcome {m.from_user.first_name}! 🌟\n\n" +
        f"This may take a moment, sit back and relax! 😊\n\n"
        f"Progress: [🟧🟧🟧🟧🟧⬜️⬜️⬜️⬜️⬜️] 50%\n\n"
    )

    await asyncio.sleep(1)
    await start_message.edit_text(
        f"🌟 Welcome {m.from_user.first_name}! 🌟\n\n" +
        f"Checking subscription status... 🔍\n\n"
        f"Progress: [🟨🟨🟨🟨🟨🟨🟨🟨⬜️⬜️] 75%\n\n"
    )

    await asyncio.sleep(1)
    if m.chat.id in AUTH_USERS:
        await start_message.edit_text(
            f"🌟 Welcome {m.from_user.first_name}! 🌟\n\n" +
            f"Great! You are a premium member!\n"
            f"Use Command : /help to get started 🌟\n\n"
            f"If you face any problem contact -  [ADMIN](http://t.me/contact_262524_bot)\n", disable_web_page_preview=True, reply_markup=BUTTONSCONTACT
        )
    else:
        await asyncio.sleep(2)
        await start_message.edit_text(
        f" 🎉 Welcome {m.from_user.first_name} to DRM Bot! 🎉\n\n"
           f"You can have access to download all Non-DRM+AES Encrypted URLs 🔐 including\n\n"
           f"Use Command : /help to get started 🌟\n\n"
           f"• 🧑‍🏫 Ph*j*CsW*llah DRM\n"
           f"• 🎓 All Non DRM+AES Encrypted URLs\n"
           f"• 🎓 MPD URLs if the key is known (e.g., Mpd_url?key=key XX:XX)\n\n"
           f"<blockquote>💵 Monthly Plan: ₹100</blockquote>\n\n"
           f"If you want to buy membership of the bot, feel free to contact the Bot Admin.\n", disable_web_page_preview=True, reply_markup=keyboard
    )


@bot.on_message(filters.command(["id"]))
async def id_command(client, message: Message):
    chat_id = message.chat.id
    await message.reply_text(f"<blockquote>The ID of this chat id is:</blockquote>\n`{chat_id}`")

@bot.on_message(filters.private & filters.command(["info"]))
async def info(bot: Client, update: Message):

    text = (
        f"╭────────────────╮\n"
        f"│✨ **Your Telegram Info**✨ \n"
        f"├────────────────\n"
        f"├🔹**Name :** `{update.from_user.first_name} {update.from_user.last_name if update.from_user.last_name else 'None'}`\n"
        f"├🔹**User ID :** @{update.from_user.username}\n"
        f"├🔹**TG ID :** `{update.from_user.id}`\n"
        f"├🔹**Profile :** {update.from_user.mention}\n"
        f"╰────────────────╯"
    )

    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=BUTTONSCONTACT
    )

@bot.on_message(filters.command(["help"]))
async def txt_handler(client: Client, m: Message):
    await bot.send_message(m.chat.id, text= (
        f"╭━━━━━━━✦✧✦━━━━━━━╮\n"
        f"💥 𝘽𝙊𝙏𝙎 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦\n"
        f"╰━━━━━━━✦✧✦━━━━━━━╯\n"
        f"▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n" 
        f"📌 𝗠𝗮𝗶𝗻 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀:\n\n"  
        f"➥ /start – Bot Status Check\n"
        f"➥ /drm – Extract from .txt (Auto)\n" 
        f"➥ /id – Get Chat/User ID\n"  
        f"➥ /info – User Details\n"  
        f"➥ /stop – Cancel Running Task\n"
        f"▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n"
        f"👤 𝐔𝐬𝐞𝐫 𝐀𝐮𝐭𝐡𝐞𝐧𝐭𝐢𝐜𝐚𝐭𝐢𝐨𝐧: **(OWNER)**\n\n" 
        f"➥ /adduser xxxx – Add User ID\n" 
        f"➥ /removeuser xxxx – Remove User ID\n"  
        f"➥ /userlist – Total User List\n"  
        f"▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n"
        f"💡 𝗡𝗼𝘁𝗲:\n\n"  
        f"• Please Support Devloper\n"  
        f"╭────────⊰◆⊱────────╮\n"   
        f" ➠ 𝐌𝐚𝐝𝐞 𝐁𝐲 : {CREDIT} 💻\n"
        f"╰────────⊰◆⊱────────╯\n"
        )
    )                    


@bot.on_message(filters.command(["drm"]) )
async def txt_handler(bot: Client, m: Message):  
    editable = await m.reply_text(f"__Hii, I am drm Downloader Bot__\n\n<i>Send Me Your txt file which enclude Name with url...\nE.g: Name: Link</i>")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)
    file_name, ext = os.path.splitext(os.path.basename(x))  # Extract filename & extension
    path = f"./downloads/{m.chat.id}"
    pdf_count = 0
    img_count = 0
    other_count = 0

    try:    
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")

        links = []
        for i in content:
            if "://" in i:
                url = i.split("://", 1)[1]
                links.append(i.split("://", 1))
                if ".pdf" in url:
                    pdf_count += 1
                elif url.endswith((".png", ".jpeg", ".jpg")):
                    img_count += 1
                else:
                    other_count += 1
        os.remove(x)
    except:
        await m.reply_text("<pre><code>🔹Invalid file input.</code></pre>")
        os.remove(x)
        return

    await editable.edit(f"Total 🔗 links found are {len(links)}\nSend From where you want to download.initial is 1")
    if m.chat.id not in AUTH_USERS:
        print(f"User ID not in AUTH_USERS", m.chat.id)
        await bot.send_message(m.chat.id, f"__Oopss! You are not a Premium member __\n__PLEASE /upgrade YOUR PLAN__\n__Send me your user id for authorization__\n__Your User id__ - `{m.chat.id}`\n")
        return
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("__Enter Batch Name or send /d for grabbing from text filename.__")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    if raw_text0 == '/d':
        b_name = file_name.replace('_', ' ')
    else:
        b_name = raw_text0

    await editable.edit("__Enter resolution or Video Quality (`144`, `240`, `360`, `480`, `720`, `1080`)__")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    quality = f"{raw_text2}p"
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"

    await editable.edit("__Enter Your Channel Name or Owner Name__\n__Send /d for use default__")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    if raw_text3 == '/d':
        CR = f"{CREDIT}"
    else:
        CR = raw_text3

    await editable.edit("🔹Enter Your PW Token For 𝐌𝐏𝐃 𝐔𝐑𝐋\n🔹Send /anything for use default")
    input4: Message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text
    await input4.delete(True)

    await editable.edit(f"Send the Video Thumb URL\nSend /d for use default\n\nYou can direct upload thumb\nSend **No** for use default")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)

    if input6.photo:
        thumb = await input6.download()  # Use the photo sent by the user
    elif raw_text6.startswith("http://") or raw_text6.startswith("https://"):
        # If a URL is provided, download thumbnail from the URL
        getstatusoutput(f"wget '{raw_text6}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb = raw_text6

    await editable.edit("__Please Provide Channel id or where you want to Upload video or Sent Video otherwise /d __\n\n__And make me admin in this channel then i can able to Upload otherwise i can't__")
    input7: Message = await bot.listen(editable.chat.id)
    raw_text7 = input7.text
    if "/d" in input7.text:
        channel_id = m.chat.id
    else:
        channel_id = input7.text
    await input7.delete()     
    await editable.delete()

    if "/d" in raw_text7:
        batch_message = await m.reply_text(f"<b>🎯Target Batch : {b_name}</b>")
    else:
        try:
            batch_message = await bot.send_message(chat_id=channel_id, text=f"<b>🎯Target Batch : {b_name}</b>")
            await bot.send_message(chat_id=m.chat.id, text=f"<b><i>🎯Target Batch : {b_name}</i></b>\n\n🔄 Your Task is under processing, please check your Set Channel📱. Once your task is complete, I will inform you 📩")
        except Exception as e:
            await m.reply_text(f"**Fail Reason »** {e}\n")
            return

    failed_count = 0
    count =int(raw_text)    
    arg = int(raw_text)
    try:
        for i in range(arg-1, len(links)):
            Vxy = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","")
            url = "https://" + Vxy
            link0 = "https://" + Vxy

            name1 = links[i][0].replace("(", "[").replace(")", "]").replace("_", "").replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'TEAM LB ❤️ {name1[:60]}'

            if "childId" in url and "parentId" in url:
                url = f"https://anonymousrajputplayer-9ab2f2730a02.herokuapp.com/pw?url={url}&token={raw_text4}"

            elif "d1d34p8vz63oiq" in url or "sec1.pw.live" in url:
                url = f"https://anonymouspwplayer-b99f57957198.herokuapp.com/pw?url={url}?token={raw_text4}"

            if "youtu" in url:
                ytf = f"bv*[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[height<=?{raw_text2}]"
            elif "embed" in url:
                ytf = f"bestvideo[height<={raw_text2}]+bestaudio/best[height<={raw_text2}]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            elif "webvideos.classplusapp." in url:
               cmd = f'yt-dlp --add-header "referer:https://web.classplusapp.com/" --add-header "x-cdn-tag:empty" -f "{ytf}" "{url}" -o "{name}.mp4"'
            elif "youtube.com" in url or "youtu.be" in url:
                cmd = f'yt-dlp --cookies youtube_cookies.txt -f "{ytf}" "{url}" -o "{name}".mp4'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:
                cc = f'[🎥]Vid Id : {str(count).zfill(3)}\n**Video Title :** {name1}\n\n<pre><code>**Batch Name :** {b_name}</code></pre>\n**Contact ➤** {CR} \n\n {ALL}   {YT} \n '
                cc1 = f'[📕]Pdf Id : {str(count).zfill(3)}\n**File Title :** {name1}\n\n<pre><code>**Batch Name :** {b_name}</code></pre>\n**Contact ➤** {CR} \n\n {ALL}   {YT} \n '

                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=channel_id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue    

                elif ".pdf" in url:
                    if "cwmediabkt99" in url:
                        max_retries = 15  # Define the maximum number of retries
                        retry_delay = 4  # Delay between retries in seconds
                        success = False  # To track whether the download was successful
                        failure_msgs = []  # To keep track of failure messages

                        for attempt in range(max_retries):
                            try:
                                await asyncio.sleep(retry_delay)
                                url = url.replace(" ", "%20")
                                scraper = cloudscraper.create_scraper()
                                response = scraper.get(url)

                                if response.status_code == 200:
                                    with open(f'{name}.pdf', 'wb') as file:
                                        file.write(response.content)
                                    await asyncio.sleep(retry_delay)  # Optional, to prevent spamming
                                    copy = await bot.send_document(chat_id=channel_id, document=f'{name}.pdf', caption=cc1,)
                                    count += 1
                                    os.remove(f'{name}.pdf')
                                    success = True
                                    break  # Exit the retry loop if successful
                                else:
                                    failure_msg = await m.reply_text(f"Attempt {attempt + 1}/{max_retries} failed: {response.status_code} {response.reason}")
                                    failure_msgs.append(failure_msg)

                            except Exception as e:
                                failure_msg = await m.reply_text(f"Attempt {attempt + 1}/{max_retries} failed: {str(e)}")
                                failure_msgs.append(failure_msg)
                                await asyncio.sleep(retry_delay)
                                continue 
                        for msg in failure_msgs:
                            await msg.delete()

                    else:
                        try:
                            cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                            download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                            os.system(download_cmd)
                            copy = await bot.send_document(chat_id=channel_id, document=f'{name}.pdf', caption=cc1)
                            count += 1
                            os.remove(f'{name}.pdf')
                        except FloodWait as e:
                            await m.reply_text(str(e))
                            time.sleep(e.x)
                            continue    

                else:
                    Show = f"__**Video Downloading__**\n<pre><code>{str(count).zfill(3)}) {name1}</code></pre>"
                    prog = await bot.send_message(channel_id, Show, disable_web_page_preview=True)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog, channel_id)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await bot.send_message(channel_id, f'⚠️**Downloading Failed**⚠️\n**Name** =>> `{str(count).zfill(3)} {name1}`\n**Url** =>> {link0}\n\n<pre><i><b>Failed Reason: {str(e)}</b></i></pre>', disable_web_page_preview=True)
                count += 1
                failed_count += 1
                continue

    except Exception as e:
        await m.reply_text(e)
        time.sleep(2)

    success_count = len(links) - failed_count
    if raw_text7 == "/d":
        await bot.send_message(channel_id, f"**-┈━═.•°✅ Completed ✅°•.═━┈-**\n\n**🎯Batch Name : {b_name}**\n🔗 Total URLs: {len(links)} \n┃   ┠🔴 Total Failed URLs: {failed_count}\n┃   ┠🟢 Total Successful URLs: {success_count}\n┃   ┃   ┠🎥 Total Video URLs: {other_count}\n┃   ┃   ┠📄 Total PDF URLs: {pdf_count}\n┃   ┃   ┠📸 Total IMAGE URLs: {img_count}\n")
    else:
        await bot.send_message(channel_id, f"**-┈━═.•°✅ Completed ✅°•.═━┈-**\n\n**🎯Batch Name : {b_name}**\n<blockquote>🔗 Total URLs: {len(links)} \n┃   ┠🔴 Total Failed URLs: {failed_count}\n┃   ┠🟢 Total Successful URLs: {success_count}\n┃   ┃   ┠🎥 Total Video URLs: {other_count}\n┃   ┃   ┠📄 Total PDF URLs: {pdf_count}\n┃   ┃   ┠📸 Total IMAGE URLs: {img_count}</blockquote>\n")
        await bot.send_message(m.chat.id, f"<blockquote><b>✅ Your Task is completed, please check your Set Channel📱</b></blockquote>")


def reset_and_set_commands():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/setMyCommands"
    # Reset
    requests.post(url, json={"commands": []})
    # Set new
    commands = [
        {"command": "start", "description": "✅ Check Alive the Bot"},
        {"command": "help", "description": "☰ Bot Usage Details"},
        {"command": "drm", "description": "📑 Upload .txt file"},
        {"command": "info", "description": "ℹ️ Check Your Information"},
        {"command": "stop", "description": "🚫 Stop the ongoing process"},
        {"command": "adduser", "description": "▶️ Add User (OWNER)"},
        {"command": "removeuser", "description": "⏸️ Remove User (OWNER)"},
        {"command": "userlist", "description": "👨‍👨‍👧‍👦 All Users ID (OWNER)"}

    ]
    requests.post(url, json={"commands": commands})

if __name__ == "__main__":
    reset_and_set_commands()
bot.run()
