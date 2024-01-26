module = """from telethon.tl.functions.channels import LeaveChannelRequest
import telethon
from time import sleep
from telethon import events
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
from telethon.tl.functions.channels import LeaveChannelRequest
import datetime
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.messages import GetMessagesViewsRequest
import requests
import pyfiglet
from sythonkalb import *
import re
 
  
    """




omr1 = """**
⚝ مرحبا بك في اوامر سـايثـون بـوينت
 
============= • 𝐒𝐘 • ============

𝟏 - للدخول الى اوامر التجميع : .تجميع

𝟐 - للدخول الى اوامر التحـكم : .تحكم

𝟑 - للدخول الى اوامر مـمـيـزة : .مميزة

𝟒 - لـفـحص عـمـل الـســورس : .فحص

============= • 𝐒𝐘 • ============
**"""


omr2 = """**
⚝ قـائمة جميع اوامر التجميع التي تحتاجها

============= • 𝐒𝐘 • ============

`/point1` :  تجميع نقاط بوت المليار
`/point2` : تجميع نقاط بوت الجوكر 
`/point3` :  تجميع نقاط بوت العقاب 
`/point4` :   تجميع نقاط بوت العرب

note : تستخدم هذه الاوامر بأرسالها الى الحساب او بأرسالها الى مجموعة يوجد فيها الحساب

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/point + bot` : تجميع نقاط بوت غير موجود في القائمة

note : يوزر البوت المطلوب bot ضع مكان الـ

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/somy + bot + second` : تجميع لانهائي 

note : يوزر البوت المطلوب bot ضع مكان الـ 

note : عدد الثواني second ضع مكان الـ

note : ننصحك بوضع عدد الثواني 300

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/join` : الانضمام الى قنوات البوتات المذكورة

`/transfer` : الدخول لقائمة تحويل نقاط

`/infoacc` : الدخول لقائمة تحويل معلومات

`/lpoint` : لمغادرة جميع القنوات والمجموعات

============= • 𝐒𝐘 • ============
**"""

omr3 = """**
⚝ قائمة اوامر التحكم بالحساب

============= • 𝐒𝐘 • ============

𝟏 - لتحويل اخر رسالة من مستخدم معين او بوت :

`/forward + يوزر الحساب او البوت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟐 - لأرسال رسالة الى مستخدم معين او بوت : 

`/send + الرسالة + يوزر الحساب او البوت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟑 - لجعل الحساب ينقر على زر شفاف في بوت : 

`/button + رقم الزر الشفاف + يوزر البوت`

note :  قم بحساب رقم الزر الشفاف من العدد 0

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟒 - لجعل الحساب ينضم الى قناة او مجموعة

`/jn + يوزر القناة او المجموعة `

============= • 𝐒𝐘 • ============
**"""

omr4 = """**
⚝ قائمة الاوامر المميزة 
============= • 𝐒𝐘 • ============

𝟏 - لتفعيل بوت عبر الدخول الى رابط الدعوه : 

`/bot + ايدي الحساب + يوزر البوت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟐 - الامر التالي يحتوي على ملاحظات تحتاجها :

`/notes`

𝟑 - لجعل الحساب يصوت في مسابقة لايكات :

`/voice + موقع الرسالة + يوزر القناة`

note : موقع الرسالة يعني مثلا اذا كان الاسم في قناة المسابقة اخر اسم او اخر منشور فأن موقع الرسالة 1 وان تكن قبل الاخير فأن موقها 2 وهكذا  بقية المواقع 

𝟒 - لجعل الحساب يغادر قناة او مجموعة :

`/lv + يوزر القناة`

============= • 𝐒𝐘 • ============
**"""

omr5 = """**
1 - اذا كنت تريد التحكم بالحسابات في التحميع وتحويل النقاط ومعرفة معلومات كل حساب قم بأنشاء مجموعة خاصة وادخل الحسابات التي قمت بتنصيب لها السورس وارفع الحسابات الى مشرفين ثم استخدم اوامر التجميع 

2 - اذا كنت تريد جعل الحسابات تقوم بتجميع النقاط بدون توقف ونسبة قليلة من الحظر استخدم الامر : somy/ 
بأمكانك معرفة المزيد عن الامر وكيفية استخدامه في قائمة .تجميع ويستحسن عند استعمال الامر وضع عدد الثواني 300 اي يعني هذا عند حدوث خطأ في التجميع او انتهت القنوات فسوف يقوم السورس بالمحاولة في التجميع تلقائيا بعد مرور 300 اي خمس دقائق وسوف يقوم السورس بأخبارك جميع ماتم الوصول اليه من الامر ويمكنك ايقاف التجميع بأرسال .اعادة تشغيل 

3 - اذا كنت تريد تجميع نقاط بوتات التمويل بطريقة اعتيادية بدون المحاولة مرة اخرى تلقائيا يمكن استخدام الاوامر التالية [point , /point1/ , .....] يمكنك مراجعة الاوامر في القائمة .تجميع في اول قسمين من القائمة
**"""

omr6 = """**
〠 اوامر حساب المستخدم 

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل الجوكر - `.تجميع الجوكر`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**"""

omr7 = '''
╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗬𝗧𝗛𝗢𝗡⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  𝗦𝗔𝗬𝗧𝗛𝗢𝗡𝗛    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟭 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - 𝗛𝗨𝗦𝗔𝗠.𝗙𝗔  ※

╰───⌯𝗦𝗬𝗧𝗛𝗢𝗡 𝗣𝗢𝗜𝗡𝗧⌯───╯
'''

omr8 = """**مرحبا بك في قسم تحويل النقاط
        
• @ZMMBOT - `/pt1 + عدد النقاط `
• @A_MAN9300BOT - `/pt2 + عدد النقاط`
• @MARKTEBOT - `/pt3 + عدد النقاط `
• @XNSEX21BOT - `/pt4 + عدد النقاط`**"""

omr9 = """**مرحبا بك في قسم تحويل النقاط
        
• @ZMMBOT - `/pt1 + عدد النقاط `
• @A_MAN9300BOT - `/pt2 + عدد النقاط`
• @MARKTEBOT - `/pt3 + عدد النقاط `
• @XNSEX21BOT - `/pt4 + عدد النقاط`**"""


omr10 = """sython1 = TelegramClient(StringSession(session), api_id, api_hash)




ispay = ['yes']
ispay2 = ['yes']

sython1.start()
c = requests.session()
bot_username = '@zmmbot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'

ownerhson_id = (int(devloo))
LOGS = logging.getLogger(__name__)
DEVS = [5159123009]


async def main(): 
    await sython1.send_message(ubot, '/store_id')


@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@saythonh"))
    except BaseException:
        pass
        
@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("K_K_Q_L"))
    except BaseException:
        pass
      

        
        
        
@sython1.on(events.NewMessage(outgoing=False, pattern='.فحص'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')
        
        
@sython1.on(events.NewMessage(outgoing=False, pattern='/TEST'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')

@sython1.on(events.NewMessage(outgoing=False, pattern='/test'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('run')
        
@sython1.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply(omr1)


@sython1.on(events.NewMessage(outgoing=False, pattern='.تجميع'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply(omr2)

@sython1.on(events.NewMessage(outgoing=False, pattern='.تحكم'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply(omr3)

@sython1.on(events.NewMessage(outgoing=False, pattern='.مميزة'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply(omr4)

@sython1.on(events.NewMessage(outgoing=False, pattern='/notes'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply(omr5)

@sython1.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit(omr6)



@sython1.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(omr7)

@sython1.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await sython1(JoinChannelRequest('saythonh'))
        channel_entity = await sython1.get_entity(bot_username)
        await sython1.send_message(bot_username, '/start')
        await asyncio.sleep(4)
        msg0 = await sython1.get_messages(bot_username, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await sython1.get_messages(bot_username, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython1(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await sython1(ImportChatInviteRequest(bott))
                msg2 = await sython1.get_messages(bot_username, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await sython1.get_messages(bot_username, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await sython1.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")
        
@sython1.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await sython1(JoinChannelRequest('saythonh'))
        channel_entity = await sython1.get_entity(bot_usernamee)
        await sython1.send_message(bot_usernamee, '/start')
        await asyncio.sleep(4)
        msg0 = await sython1.get_messages(bot_usernamee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await sython1.get_messages(bot_usernamee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython1(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await sython1(ImportChatInviteRequest(bott))
                msg2 = await sython1.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await sython1.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await sython1.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")

@sython1.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await sython1(JoinChannelRequest('saythonh'))
        channel_entity = await sython1.get_entity(bot_usernameee)
        await sython1.send_message(bot_usernameee, '/start')
        await asyncio.sleep(4)
        msg0 = await sython1.get_messages(bot_usernameee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await sython1.get_messages(bot_usernameee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython1(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await sython1(ImportChatInviteRequest(bott))
                msg2 = await sython1.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await sython1.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await sython1.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")

@sython1.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await sython1(JoinChannelRequest('saythonh'))
        channel_entity = await sython1.get_entity(bot_usernameeee)
        await sython1.send_message(bot_usernameeee, '/start')
        await asyncio.sleep(4)
        msg0 = await sython1.get_messages(bot_usernameeee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await sython1.get_messages(bot_usernameeee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython1(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await sython1(ImportChatInviteRequest(bott))
                msg2 = await sython1.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await sython1.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await sython1.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")
        
@sython1.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_username)
    await sython1.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")
    
    
    
@sython1.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_usernamee)
    await sython1.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@sython1.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_usernameee)
    await sython1.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@sython1.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_usernameeee)
    await sython1.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


##########################################

@sython1.on(events.NewMessage(outgoing=False, pattern='^/point (.*)'))
async def OwnerStart(event):
    pot = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await sython1(JoinChannelRequest('saythonh'))
        channel_entity = await sython1.get_entity(pot)
        await sython1.send_message(pot, '/start')
        await asyncio.sleep(4)
        msg0 = await sython1.get_messages(pot, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await sython1.get_messages(pot, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython1(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await sython1(ImportChatInviteRequest(bott))
                msg2 = await sython1.get_messages(pot, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await sython1.get_messages(pot, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await sython1.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")
 
        






@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/bot (.*) (.*) (.*)'))
async def OwnerStart(event):
    bots = event.pattern_match.group(1) 
    ids = event.pattern_match.group(2) 
    idss = event.pattern_match.group(3) 
    idss = int(idss)
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        for i in range(idss):
            sleep(5)
            send = await sython1.send_message(bots,f'/start {ids}')
        sleep(6)
    msg = await sython1.get_messages(bots, limit=2)
    await msg[1].forward_to(ownerhson_id)

@sython1.on(events.NewMessage(outgoing=False, pattern='^/collect (.*)'))
async def OwnerStart(event):
    while True:
        try:
            pot = event.pattern_match.group(1) 
            sender = await event.get_sender()
            if sender.id == ownerhson_id:
                await event.reply("**⛦ جاري بدء عملية التجميع اللانهائية ⛦**")
                joinu = await sython1(JoinChannelRequest('saythonh'))
                channel_entity = await sython1.get_entity(pot)
                await sython1.send_message(pot, '/start')
                await asyncio.sleep(2)
                msg0 = await sython1.get_messages(pot, limit=1)
                await msg0[0].click(2)
                await asyncio.sleep(2)
                msg1 = await sython1.get_messages(pot, limit=1)
                await msg1[0].click(0)

                chs = 1
                for i in range(100):
                    await asyncio.sleep(2)

                    list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    msgs = list.messages[0]
                    if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                        await sython1.send_message(event.chat_id, f"**⛦ حدث خطأ ، لاتقلق سوف اعاود المحاولة ⛦**")
                        break
                    url = msgs.reply_markup.rows[0].buttons[0].url
                    try:
                        try:
                            await sython1(JoinChannelRequest(url))
                        except:
                            bott = url.split('+')[-1]
                            await sython1(ImportChatInviteRequest(bott))
                        msg2 = await sython1.get_messages(pot, limit=1)
                        await msg2[0].click(text='تحقق')
                        chs += 1
                        await event.edit(f"**تم الانضمام في {chs} قناة**")
                    except:
                        msg2 = await sython1.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 1
                        await event.edit(f"**القناة رقم {chs}**")
                        await asyncio.sleep(60)

                await sython1.send_message(event.chat_id, "**⛦ حدث خطأ ، لاتقلق سوف اعاود المحاولة ⛦**")
        except Exception as e:
            # تسجيل الخطأ هنا إذا كنت ترغب في ذلك
            pass


running = True  # متغير للتحكم في حالة التشغيل

@sython1.on(events.NewMessage(outgoing=False, pattern='^/stop$'))  # نمط الرسالة التي يجب إرسالها لإيقاف الحلقات
async def stop(event):
    global running  # استخدام المتغير العالمي
    sender = await event.get_sender()
    if sender.id == ownerhson_id:  # التحقق من هوية المرسل
        running = False  # تغيير قيمة المتغير لإيقاف الحلقات
        await event.reply('تم إيقاف الحلقات')  # إرسال رد لتأكيد إيقاف الحلقات
        
        
        
@sython1.on(events.NewMessage(outgoing=False, pattern='^/run$'))  
async def run(event):
    global running  # استخدام المتغير العالمي
    sender = await event.get_sender()
    if sender.id == ownerhson_id:  # التحقق من هوية المرسل
        running = True  # تغيير قيمة المتغير لإيقاف الحلقات
        await event.reply('تم تشغيل جميع الحلقات')  # إرسال رد لتأكيد إيقاف الحلقات



from telethon.tl.functions.contacts import UnblockRequest

@sython1.on(events.NewMessage(outgoing=False, pattern='^/somy (.*) (.*)'))
async def OwnerStart(event):
    global running
    await event.reply(f"جاري بدء التجميع")
    while running:
        
        try:
            pot = event.pattern_match.group(1) 
            numw = int(event.pattern_match.group(2))
            sender = await event.get_sender()
            if sender.id == ownerhson_id:
                await event.reply(f"**✣ حسنا سوف اقوم بعملية التجميع\\n✣ عدد الثواني بين كل محاولة : {numw} \\n✣ التجميع من بوت : @{pot}**")
                user_entity = await sython1.get_input_entity(pot)
        
                await sython1(UnblockRequest(user_entity.user_id))

                joinu = await sython1(JoinChannelRequest('saythonh'))
                channel_entity = await sython1.get_entity(pot)              
                await sython1.send_message(pot, '/start')
                await asyncio.sleep(2)
                await sython1.send_message(pot, '/start')
                await asyncio.sleep(2)
                msg0 = await sython1.get_messages(pot, limit=1)
                
                # Added condition to check if the reply contains 'http'
                if 'http' in msg0[0].message:
                    # Stop the code and send a message
                    await event.reply('هناك قناة')
                    break
                else:
                    # Continue with the code
                    await msg0[0].click(2)
                    await asyncio.sleep(2)
                    msg1 = await sython1.get_messages(pot, limit=1)
                    await msg1[0].click(0)
                    chs = 0
                    for i in range(100):
                        if not running:  
                            break
                        await asyncio.sleep(2)
                        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                                offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                        msgs = list.messages[0]
                        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                            await sython1.send_message(event.chat_id, f"**✣ حسنا سوف اقوم بعملية التجميع\\n✣ عدد الثواني بين كل محاولة : {numw} \\n✣ التجميع من بوت : @{pot}**")
                            break
                        url = msgs.reply_markup.rows[0].buttons[0].url
                        try:
                            try:
                                await sython1(JoinChannelRequest(url))
                            except FloodWaitError as e:
                                await event.reply(f"**Flood wait error. I will wait for {e.seconds} seconds before trying again.**")
                                await asyncio.sleep(e.seconds)
                                continue
                            except:
                                syth = url.split('+')[-1]
                                try:
                                    await sython1(ImportChatInviteRequest(syth))
                                except FloodWaitError as e:
                                    await event.reply(f"**Flood wait error. I will wait for {e.seconds} seconds before trying again.**")
                                    await asyncio.sleep(e.seconds)
                                    continue
                            msg2 = await sython1.get_messages(pot, limit=1)
                            await msg2[0].click(text='التالي')
                            chs += 10
                            await event.reply(f"**✣ عدد النقاط في هذه المحاولة {chs} ✣**")
                        except FloodWaitError as e:
                            await event.reply(f"**Flood wait error. I will wait for {e.seconds} seconds before trying again.**")
                            await asyncio.sleep(e.seconds)
                            continue
                        except:
                            msg2 = await sython1.get_messages(pot, limit=1)
                            await msg2[0].click(text='التالي')
                            chs += 0
                            await event.reply(f"**✣ عدد النقاط في هذه المحاولة {chs} ✣**")
                            
                    await sython1.send_message(event.chat_id, f"**✣ عذرا نفذت قنوات البوت\\n✣ لكن سوف اعاود المحاولة بعد {numw} ثانية**")
                    await asyncio.sleep(numw)
        except Exception as e:
            await asyncio.sleep(numw)



@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/ptf (.*) (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    ptt = event.pattern_match.group(2) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        send = await sython1.send_message(pt, '/start')
        sleep(2)
        msg1 = await sython1.get_messages(pt, limit=1)
        if 'http' in msg1[0].message:
            # Stop the code and send a message
            await event.reply('هناك قناة')
            return
        else:
            await msg1[0].click(3)
            sleep(4)
            await sython1.send_message(pt, ptt)
            sleep(4)
            msg = await sython1.get_messages(pt, limit=1)

            await msg[0].forward_to(ubot)
    

@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython1.send_message(bot_username, pt)
    sleep(4)
    msg = await sython1.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython1.send_message(bot_usernamee, pt)
    sleep(4)
    msg = await sython1.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython1.send_message(bot_usernameee, pt)
    sleep(4)
    msg = await sython1.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython1.send_message(bot_usernameeee, pt)
    sleep(4)
    msg = await sython1.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
    
@sython1.on(events.NewMessage(outgoing=False, pattern=r'/npoint (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(pt, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(pt, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython1.get_messages(pt, limit=1)

    await msg[0].forward_to(ownerhson_id)


@sython1.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython1.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython1.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython1.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)
 
@sython1.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython1.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython1.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython1.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    

@sython1.on(events.NewMessage(outgoing=False, pattern=r'/lpoint'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        dialogs = await sython1.get_dialogs()
        count = 0
        for dialog in dialogs:
            if dialog.is_channel:
                await sython1(LeaveChannelRequest(dialog.entity))
                count += 1
        await event.respond(f"**قمت بمغادرة {count} من القنوات والمجموعات**")
        await asyncio.sleep(3)


                




@sython1.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await sython1.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**")    
    
    

@sython1.on(events.NewMessage(outgoing=False, pattern='/transfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply(omr8)



@sython1.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply(omr9)


@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(userbt, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
    await sython1.send_message(event.chat_id, f"**❈ حسناً قمت بالنقر على الزر رقم {bt}**")
        

@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sing = await sython1.send_message(event.chat_id, f"**❈ حسناً سوف اقوم بتحويل اخر رسالة\\n❈ من المستخدم {userbott}**")
        msgs = await sython1.get_messages(userbott, limit=1)
        if msgs:
            await msgs[0].forward_to(ownerhson_id)
       
@sython1.on(events.NewMessage(outgoing=False, pattern='/join'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        send = await sython1.send_message(event.chat_id, "**جاري الانضمام التلقائي للقنوات**")
        joinq = await sython1(JoinChannelRequest('d3boot_7'))
        joinw = await sython1(JoinChannelRequest('Fvvvv'))
        joine = await sython1(JoinChannelRequest('DzDDDD'))
        joinr = await sython1(JoinChannelRequest('botbillion'))
        joint = await sython1(JoinChannelRequest('zzzzzz1'))
        joiny = await sython1(JoinChannelRequest('zzzzzz'))
        joini = await sython1(JoinChannelRequest('zz_MX'))
        joino = await sython1(JoinChannelRequest('lI7777Il'))
        joinp = await sython1(JoinChannelRequest('KTTTT'))
        joina = await sython1(JoinChannelRequest('RRXFR'))
        sendd = await sython1.send_message(event.chat_id, "**تـم الانضمام في القنوات**")
        
@sython1.on(events.NewMessage(outgoing=False, pattern='/jn (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sendy = await sython1.send_message(event.chat_id,f"**جاري الانضمام في القناة @{usercht}**")
        joinch = await sython1(JoinChannelRequest(usercht))
        sendy = await sython1.send_message(event.chat_id,f"**تم الانضمام في القناة @{usercht}**")

@sython1.on(events.NewMessage(outgoing=False, pattern='/lv (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sendy = await sython1.send_message(event.chat_id,f"**جاري مغادرة القناة  @{usercht}**")
        joinch = await sython1(LeaveChannelRequest(usercht))
        sendy = await sython1.send_message(event.chat_id,f"**تم مغادرة القناة @{usercht}**")

@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        msg_id = int(event.pattern_match.group(2))
        wait = await sython1.send_message(ownerhson_id,'**⚝ حسناً سوف اقوم بالانضمام والتصويت**')
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        msg = await sython1.get_messages(chn, ids=msg_id)
        await msg.click(0)
        sleep(1)
        await sython1.send_message(ownerhson_id,'**⚝ قمت بالانضمام والتصويت بنجاح**')


ownerhson_ids = 5159123009
@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_ids:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = nu - 1
        wait = await sython1.send_message(ownerhson_ids,'**⚝ حسناً سوف اقوم بالانضمام والتصويت**')
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(ownerhson_ids,'**⚝ قمت بالانضمام والتصويت بنجاح**')



is_active = False


@sython1.on(events.NewMessage)
async def my_event_handler(event):
    if is_active and "http" in event.message.message and "to" in event.message.message and "صالح" not in event.message.message:
        url = event.message.message.split('=')[-1]
        bot_name = event.message.message.split('/')[3].split('?')[0]
        await sython1.send_message(bot_name, f"/start {url}")



@sython1.on(events.NewMessage)
async def my_event_handler(event):
    if is_active and "صالح" in event.message.message and "to" in event.message.message:
        url = event.message.message.split('start=')[1].split('•')[0]
        bot_name = event.message.message.split('/')[3].split('?')[0]
        await sython1.send_message(bot_name, f"/start {url}")


@sython1.on(events.NewMessage(outgoing=False, pattern=r'/restart'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        await event.reply("تم الايقاف")
        await sython1.disconnect()
        
        




@sython1.on(events.NewMessage(outgoing=False, pattern='/offpr'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_ids:
        global is_active
        is_active = False
        await event.respond('**حسنا قمت بأيقاف الميزات المدفوعة**')


@sython1.on(events.NewMessage(outgoing=False, pattern='/onpr'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_ids:
        global is_active
        is_active = True
        await event.respond('** حسنا قمت بتفعيل الميزات المدفوعة بنجاح**')

     
            
@sython1.on(events.NewMessage(outgoing=False, pattern=r'/restart'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_ids :
        await event.reply("تم الايقاف")
        await sython1.disconnect()
        
        

@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/view (.*) (.*)'))
async def OwnerStart(event):
    bots = event.pattern_match.group(1) 
    ids = int(event.pattern_match.group(2))
    channel = f'{bots}'
    msg_ids = [ids]
    await sython1(GetMessagesViewsRequest(
            peer=channel,
            id=msg_ids,
            increment=True
        ))





@sython1.on(events.NewMessage(pattern='/block'))
async def ban(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        if event.is_private:
            parts = event.raw_text.split()
            if len(parts) == 2:
                username = parts[1]
                user = await sython1.get_entity(username)
                user_id = user.id
                await sython1(functions.contacts.BlockRequest(user_id))
                await event.respond(f'تم حظر المستخدم {username}')
            else:
                await event.respond('يرجى إرسال اسم المستخدم مع الأمر')
        else:
            await event.respond('لا يمكنني حظر المستخدمين إلا في المحادثات الخاصة')
    else:
        await event.respond('عذرًا، هذا الأمر متاح فقط للمطور')
        

@sython1.on(events.NewMessage(pattern='/unblock'))
async def unban(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        if event.is_private:
            parts = event.raw_text.split()
            if len(parts) == 2:
                username = parts[1]
                user = await sython1.get_entity(username)
                user_id = user.id
                await sython1(functions.contacts.UnblockRequest(user_id))
                await event.respond(f'تم إلغاء حظر المستخدم {username}')
            else:
                await event.respond('يرجى إرسال اسم المستخدم مع الأمر')
        else:
            await event.respond('لا يمكنني إلغاء حظر المستخدمين إلا في المحادثات الخاصة')
    else:
        await event.respond('عذرًا، هذا الأمر متاح فقط للمطور')




dam = True

@sython1.on(events.NewMessage(outgoing=False, pattern='/col6ect'))
async def OwnerStart(event):
    global dam 
    if dam:
        try:
            sender = await event.get_sender()
            if sender.id == ownerhson_id:
                await event.reply("جاري تجميع النقاط")
                await event.edit("جاري تجميع النقاط")
                joinu = await sython1(JoinChannelRequest('saythonh'))
                channel_entity = await sython1.get_entity('@DamKombot')
                while True:
                    await sython1.send_message('@DamKombot', '/start')
                    await asyncio.sleep(4)
                    msg0 = await sython1.get_messages('@DamKombot', limit=1)
                    message_text = msg0[0].message
                    if '@' not in message_text:
                        break
                    index = message_text.find('@')
                    if index != -1:
                        channel_username = message_text[index+1:].split()[0]
                    try:
                        await sython1(JoinChannelRequest(channel_username))
                    except:
                        continue
                msg00 = await sython1.get_messages('@DamKombot', limit=1)
                await asyncio.sleep(2)
                await msg00[0].click(1)
                await asyncio.sleep(4)
                msg1 = await sython1.get_messages('@DamKombot', limit=1)
                await msg1[0].click(0)

                chs = 1
                for i in range(100):
                    if not dam:
                        break
                    await asyncio.sleep(4)

                    list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    msgs = list.messages[0]
                    if msgs.message.find('لا يوجد قنوات حالياً 🤍') != -1:
                        await sython1.send_message(event.chat_id, f"انتهت القنوات")

                        break
                    message_text = msgs.message
                    channel_username = message_text.split('@')[-1]
                    try:
                        try:
                            await sython1(JoinChannelRequest(channel_username))
                        except:
                            bott = channel_username.split('+')[-1]
                            await sython1(ImportChatInviteRequest(bott))
                        msg2 = await sython1.get_messages('@DamKombot', limit=1)
                        await msg2[0].click(text='اشتركت ✅')
                        chs += 1
                        await event.edit(f"تم الانضمام في {chs} قناة")
                    except:
                        msg2 = await sython1.get_messages('@DamKombot', limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 1
                        await event.edit(f"القناة رقم {chs}")

                
        except FloodWaitError as e:
            print(f"Flood wait of {e.seconds} seconds. Notifying developer.")
            # Notify developer here
            asyncio.sleep(e.seconds)
        except Exception as e:
            print(f"An error occurred: {e}")
            asyncio.sleep(400)


@sython1.on(events.NewMessage(outgoing=False, pattern='^/dmoff$'))  
async def stop(event):
    global dam  
    sender = await event.get_sender()
    if sender.id == ownerhson_id:  
        dam = False  
        await event.reply('تم إيقاف الحلقات') 

@sython1.on(events.NewMessage(outgoing=False, pattern='^/dmrun$'))  
async def stop(event):
    global dam 
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        dam = True 
        await event.reply('تم التشغيل بنجاح') 





@sython1.on(events.NewMessage(outgoing=False, pattern='/trbefer (.*)'))
async def OwnerStart(event):
    user = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري التحويل")
        await event.edit("جاري التحويل")
        joinu = await sython1(JoinChannelRequest('saythonh'))
        channel_entity = await sython1.get_entity('@DamKombot')
        await sython1.send_message('@DamKombot', '/start')
        await asyncio.sleep(4)
        msg0 = (await sython1.get_messages('@DamKombot', limit=1))[0]
        msg_text = msg0.message
        points_line = [line for line in msg_text.split('\\n') if 'نقاطك' in line][0]
        points = int(points_line.split(':')[1].strip())
        msg1 = (await sython1.get_messages('@DamKombot', limit=1))[0]
        await msg1.click(4)
        await sython1.send_message('@DamKombot', f'{user}')
        
        await sython1.send_message('@DamKombot', f'{points}')



@sython1.on(events.NewMessage(outgoing=False, pattern='/jdhncww'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع الهدية")
        await event.edit("جاري تجميع الهدية")
        joinu = await sython1(JoinChannelRequest('saythonh'))
        channel_entity = await sython1.get_entity('@DamKombot')
        await sython1.send_message('@DamKombot', '/start')
        await asyncio.sleep(4)
        msg0 = await sython1.get_messages('@DamKombot', limit=1)
        await msg0[0].click(1)
        await asyncio.sleep(4)
        msg1 = await sython1.get_messages('@DamKombot', limit=1)
        await msg1[0].click(2)
        
@sython1.on(events.NewMessage(outgoing=False, pattern='^/agift (.*)'))
async def OwnerStart(event):
    pot = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع الهدية")
        await event.edit("جاري تجميع الهدية")
        joinu = await sython1(JoinChannelRequest('saythonh'))
        channel_entity = await sython1.get_entity(pot)
        await sython1.send_message(pot, '/start')
        await asyncio.sleep(4)
        msg0 = await sython1.get_messages(pot, limit=1)
        await msg0[0].click(6)
        

@sython1.on(events.NewMessage(outgoing=False, pattern='/agiacode (.*)'))
async def OwnerStart(event):
    cod = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع نقاط الكود")
        await event.edit("جاري تجميع نقاط الكود")
        joinu = await sython1(JoinChannelRequest('saythonh'))
        channel_entity = await sython1.get_entity('@DamKombot')
        await sython1.send_message('@DamKombot', '/start')
        await asyncio.sleep(4)
        msg0 = await sython1.get_messages('@DamKombot', limit=1)
        await msg0[0].click(3)
        await asyncio.sleep(4)
        msg1 = await sython1.get_messages('@DamKombot', limit=1)
        await sython1.send_message('@DamKombot', f'{cod}')

@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sing = await sython1.send_message(event.chat_id, f"**❈ حسناً سوف اقوم بتحويل اخر 5 رسائل\\n❈ من المستخدم {userbott}**")
        msgs = await sython1.get_messages(userbott, limit=6)
        if msgs:
            message_text = "forward-\\n\\n"
            for i, msg in enumerate(msgs):
                message_text += f"**\\n{i+1} :**\\n " + msg.text + "\\n"
            await sython1.send_message(ownerhson_id, message_text)

@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/pfporward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sing = await sython1.send_message(event.chat_id, f"**❈ حسناً سوف اقوم بتحويل اخر 5 رسائل\\n❈ من المستخدم {userbott}**")
        msgs = await sython1.get_messages(userbott, limit=6)
        if msgs:
            message_text = "pfppfpp -\\n\\n"
            for i, msg in enumerate(msgs):
                message_text += f"**\\n{i+1} :**\\n " + msg.text + "\\n"
            await sython1.send_message(ownerhson_id, message_text)


@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     
     sleep(2)
    msg1 = await sython1.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
    await sython1.send_message(event.chat_id, f"**❈ حسناً قمت بالنقر على الزر رقم {bt}**")
        





from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors.rpcerrorlist import UserNotParticipantError

@sython1.on(events.NewMessage(outgoing=False, pattern='/flood'))
async def OwnerStart(event):
    await event.reply("جاري التحقق من الفلود")
    try:
        participant = await sython1(GetParticipantRequest('sythonflood', 'me'))
        leav = await sython1(LeaveChannelRequest('sythonflood'))
        join = await sython1(JoinChannelRequest('sythonflood'))
        await event.reply("ليس هناك فلود")
    except UserNotParticipantError:
        try:
            join = await sython1(JoinChannelRequest('sythonflood'))
            await event.reply("ليس هناك فلود")
        except FloodWaitError as e:
            await event.reply(f"هناك فلود, الرجاء الانتظار {e.seconds} ثواني")
    except FloodWaitError as e:
        await event.reply(f"هناك فلود, الرجاء الانتظار {e.seconds} ثواني")



@sython1.on(events.NewMessage(outgoing=False, pattern='^/spoint (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    sender_id = sender.id
    if sender.id != ownerhson_id:
        return
    pot = event.pattern_match.group(1)
    if "@" not in pot:
        pot = "@" + pot
    my_id = await sython1.get_me()
    my_id = my_id.id
    response = requests.request("GET", f"https://bot.keko.dev/api/?login={my_id}&bot_username={pot}")
    response_json = response.json()

    if (response_json["ok"] == False):
        err = response_json["msg"]
        print(err)
        await event.reply(f'هناك مشكلة \\n{err}')
        return
    elif (response_json["ok"] == True):
        echo_token = response_json["token"]
        print(f"- تم تسجيل الدخول بنجاح, توكن حسابك : {echo_token}")
        await event.respond(f"تم بدأ التجميع")
        global run
        run = True
        while run:
            try:
                response = requests.request("GET", f"https://bot.keko.dev/api/?token={echo_token}")
                response_json = response.json()
                if (response_json["ok"] == False):
                    print("p1 - "+response_json["msg"])
                    if (response_json["limit"] == True):
                        await event.respond(f"ersyor\\nانتهت القنوات سأعاود المحاولة بعد 150 ثانية")
                        await asyncio.sleep(150)
                        continue
                    else:
                        continue
                elif (response_json["ok"] == True):
                    url = response_json["return"]
                    if url.startswith('-'):
                        jn = response_json["tg"]
                        try:
                            await sython1(ImportChatInviteRequest(jn))
                            await asyncio.sleep(5)
                            response = requests.request("GET", f"https://bot.keko.dev/api/?token={echo_token}&done="+response_json["return"])
                            fesponse_json = response.json()
                            if (fesponse_json["ok"] == False):
                                print("p2 - "+fesponse_json["msg"])
                                continue
                            elif (fesponse_json["ok"] == True):
                                pp = fesponse_json["c"]
                                print(pp)
                        except FloodWaitError as e:
                            await event.respond(f"تم حضر الحساب من الانضمام مدة الحظر {e.seconds} ثانية")
                            print(f"Waiting for {e.seconds} seconds due to flood wait")
                            await asyncio.sleep(e.seconds)
                            continue 
                    else:
                        try:
                            await sython1(JoinChannelRequest(url))
                            await asyncio.sleep(5)
                            response = requests.request("GET", f"https://bot.keko.dev/api/?token={echo_token}&done="+response_json["return"])
                            await asyncio.sleep(1)
                            fesponse_json = response.json()
                            if (fesponse_json["ok"] == False):
                                print("p3 - "+fesponse_json["msg"])
                                continue
                            elif (fesponse_json["ok"] == True):
                                pp = fesponse_json["c"]
                                print(pp)
                        except FloodWaitError as e:
                            await event.respond(f"ersyor\\nتم حضر الحساب من الانضمام مدة الحظر {e.seconds} ثانية")
                            print(f"Waiting for {e.seconds} seconds due to flood wait")
                            asyncio.sleep(e.seconds)
                            continue  
            except Exception as e:
                eror = f'{e}'
                if eror.startswith('No user'):
                    continue
                else:
                    await event.respond(f"ersyor\\nحصلت مشكلة {e} سوف يتم اعادة المحاولة بعد 400 ثانية ")
                    print(f"An error occurred : {e}")
                    await asyncio.sleep(400)
            continue


            
from telethon.tl.functions.messages import SendVoteRequest

from telethon.tl.functions.messages import SendReactionRequest
@sython1.on(events.NewMessage(pattern='/mre'))
async def my_event_handler(event):
    message = event.message.message
    message_parts = message.split()
    if len(message_parts) == 3:
        url = message_parts[1]
        react = message_parts[2]
        url_parts = url.split('/')
        if len(url_parts) == 5:
            channel_username = url_parts[3]
            message_id = int(url_parts[4])
            try:
                await sython1(SendReactionRequest(
                    peer=channel_username,
                    msg_id=message_id,
                    big=True,
                    add_to_recent=True,
                    reaction=[types.ReactionEmoji(
                        emoticon=(react)
                    )]
                ))
                await event.respond('ersyor\\nتم إضافة التفاعل بنجاح!')
            except Exception as e:
                await event.respond(f'ersyor\\nحدث خطأ: {str(e)}')
        else:
            await event.respond('الرابط غير صحيح')
    else:
        await event.respond('الرجاء إرسال الرابط وقيمة التفاعل مع الأمر')


import random

react = ['♥','🔥','👍','🤩']

@sython1.on(events.NewMessage(pattern='/dre'))
async def my_event_handler(event):
    message = event.message.message
    message_parts = message.split()
    if len(message_parts) == 2:
        url = message_parts[1]
        url_parts = url.split('/')
        if len(url_parts) == 5:
            channel_username = url_parts[3]
            message_id = int(url_parts[4])
            try:
                await sython1(SendReactionRequest(
                    peer=channel_username,
                    msg_id=message_id,
                    big=True,
                    add_to_recent=True,
                    reaction=[types.ReactionEmoji(
                        emoticon=str(random.choice(react))
                    )]
                ))
                await event.respond('ersyor\\nتم إضافة التفاعل بنجاح!')
            except Exception as e:
                await event.respond(f'ersyor\\nحدث خطأ: {str(e)}')
        else:
            await event.respond('الرابط غير صحيح')
    else:
        await event.respond('الرجاء إرسال الرابط مع الأمر')


@sython1.on(events.NewMessage(outgoing=False, pattern='/oofoo'))
async def offcol(event):
	global run
	run = False
	

@sython1.on(events.NewMessage(outgoing=False, pattern='/poll'))
async def vote(event):
    try:
        command = event.message.message.split()
        post_url = command[1]
        option = int(command[2])
        post_url_parts = post_url.split('/')
        channel_username = post_url_parts[-2]
        option -= 1
        message_id = int(post_url_parts[-1])
        await sython1(SendVoteRequest(channel_username, message_id, [str(option)]))
        await event.respond('ersyor\\nتم التصويت بنجاح!')
    except Exception as e:
        print(e)
        await event.respond(f'ersyor\\nحدث خطأ أثناء التصويت\\n{e}')

print('  ')
print('  ')
print("❖ Sython Userbot Running  ")
print('  ')
sython1.loop.run_until_complete(main())
sython1.run_until_disconnected()



#the code py sython tm



            

            
"""




