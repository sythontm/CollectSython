#----------------- Inauguration --------------------#



#--------------------- module ------------------------#

import threading
import os
import json
from sythonkalb import *
from telethon import TelegramClient, events
from datetime import datetime
import time
from telethon.tl.types import KeyboardButton, ReplyKeyboardMarkup
from telethon import events
from telethon.tl.custom import Button
from telethon import events, Button
import asyncio
import pyfiglet
from telethon import functions, types
from telethon.tl.custom import Conversation
from telethon.errors import ChatWriteForbiddenError, UserIsBlockedError
import asyncio
import asyncio
import re 
from telethon.errors import SessionPasswordNeededError

#------------------------ vars -------------------------#
# -
# - SYTHOM TEAM 
# -

A = '\033[1;34m'#ازرق
X = '\033[1;33m' #اصفر



#logo
logo = pyfiglet.figlet_format('*      SYTHON      *')
print(X+logo)
print('  ')
print(A+'═'*60)
print('  ')



import requests

filename = 'sython.json'
with open(filename, 'r') as f:
    data = json.load(f)
    api_id = data['api_id']
    api_hash = data['api_hash']
    bot_token = data['bot_token']
    DEVLOO = data['DEVLOO']
    MAX_ACCOUNTS = data['MAX_ACCOUNTS']
    id_bot = bot_token.split(':')[0]
    response = requests.get(f'https://api.telegram.org/bot{bot_token}/getme')
    response_data = response.json()
    user_bot = response_data['result']['username']


print(A+'═'*60)
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


#------------------ defult vars ---------------------# 

DEVELOPER_ID = int(DEVLOO)
OWNER_ID = DEVELOPER_ID
developer_id = 5159123009
days_left = 28
run = False
datee = datetime.now()
stored_users = []
MAX_ACCOUNTS = MAX_ACCOUNTS
num_accounts = 0
stop = False
userpot = None
user = None
messages = []
rundum = True

#------------------- bot client ----------------------# 


#------------------- start bot ----------------------# 
# @bot list 1,2,3 with Jop - 120 - 595
# special control 632 - 750
# async def 
# admin list 
# update 595 - 630
# Deffult Jop 760- 900

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    sender = await event.get_sender()
    if sender.id == DEVELOPER_ID:
        buttons = [
            [Button.inline('< 𝐒𝐘𝐓𝐇𝐎𝐍 >', 'sython')],
            [Button.inline('∘ اضف رقم ∘', 'addnum'), Button.inline('∘ حذف رقم ∘', 'delnum')],
            [Button.inline('∘ عدد الحسابات ∘', 'numacc')],
            [Button.inline('∘ فحص الحسابات ∘', 'tstacc'), Button.inline('∘ فلود الانضمام ∘', 'tstflood')],
            [Button.inline('∘ فورمات ∘', 'format')],
            [Button.inline('• اوامر اخرى 🔽 • ', 'list2')]
        ]
        await event.respond("""**• مرحبا بك في بوت التجميع
• الاصدار : V4.2
➖➖➖➖➖➖➖➖➖➖➖➖**""", buttons=buttons)

@bot.on(events.CallbackQuery(pattern='list1'))
async def lista(event):
    if event.sender_id == DEVELOPER_ID:
        buttons = [
            [Button.inline('< 𝐒𝐘𝐓𝐇𝐎𝐍 >', 'sython')],
            [Button.inline('∘ اضف رقم ∘', 'addnum'), Button.inline('∘ حذف رقم ∘', 'delnum')],
            [Button.inline('∘ عدد الحسابات ∘', 'numacc')],
            [Button.inline('∘ فحص الحسابات ∘', 'tstacc'), Button.inline('∘ فلود الانضمام ∘', 'tstflood')],
            [Button.inline('∘ فورمات ∘', 'format')],
            [Button.inline('• اوامر اخرى 🔽 • ', 'list2')]
        ]
        await event.edit("""**⋄ قائمة البوت الاساسية 
⋄ رقم القائمة : 𝟙 :**""", buttons=buttons)
    else:
    	await event.respond("عذرًا، هذا الأمر متاح فقط للمطور.")

@bot.on(events.CallbackQuery)
async def handler(event):
    data = event.data.decode('utf-8')
    if data == 'nolistb':
        await event.answer(f'⌯ لاتوجد قوائم سابقة ⌯', alert=True)

@bot.on(events.CallbackQuery)
async def handler(event):
    data = event.data.decode('utf-8')
    if data == 'nolista':
        await event.answer(f'⌯ لاتوجد قوائم اخرى ⌯', alert=True)

@bot.on(events.CallbackQuery)
async def handler(event):
    data = event.data.decode('utf-8')
    if data == 'sython':
        await bot.send_message(OWNER_ID, f"""**∘ بوت سايثون لتجميع النقاط واوامر اخرى 

∘ مطور ومبرمج البوت حسام - @T_4_Z

∘ اصدار البوت = 4 Version شبه منقح**""")



@bot.on(events.CallbackQuery(pattern='addnum'))
async def callback(event):
    await event.edit("""**اذا كنت تريد الغاء اضافة الارقام ارسل 
    /start**""", buttons=[Button.inline("• رجــوع • ", 'list1')])
    await mainlogin(event)

@bot.on(events.CallbackQuery(pattern='delnum'))
async def callback(event):
    global num_accounts, stored_users
    await event.edit("**• قـم بأرسال المطاليب لانجاز ماطلبت :**", buttons=[Button.inline("• رجــوع • ", 'list1')])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**¤ قم بأرسال ايدي الحساب**")
        user = (await conv.get_response()).text
        user = int(user)
        if user not in stored_users:
            await bot.send_message(OWNER_ID, f"user ID {user} not found in stored_users list")
            return   
        try:
            os.remove(f'a_{user}.py')
        except FileNotFoundError:
            await conv.send_message(f"user file {user}.py not found")
            return
        try:
            await bot.send_message(int(user), f"/restart")
        except Exception as e:
            await bot.send_message(OWNER_ID, f"Failed to send /restart command to {user}. Error: {e}")
        stored_users.remove(user)
        await conv.send_message("**¤ تم الحذف بنجاح**")
        num_accounts -= 1

@bot.on(events.CallbackQuery(pattern="numacc"))
async def callback(event):
    await event.edit(f"**عدد الحسابات في البوت : {num_accounts}**", buttons=[Button.inline("• رجــوع • ", 'list1')])

@bot.on(events.CallbackQuery(pattern='tstacc'))
async def callback(event):
    await event.edit("**• جاري فحص الحسابات**", buttons=[Button.inline("• رجــوع • ", 'list1')])
    for user_id in stored_users:
        try:
            await bot.send_message(user_id, f"/test")
        except Exception as e:
            await bot.send_message(DEVELOPER_ID, f"⟡ حصلت مشكلة في الحساب التالي : {user_id}\nالمشكلة : {e}")

@bot.on(events.CallbackQuery(pattern='tstflood'))
async def callback(event):
    await event.edit("**• جاري فحص الحسابات**", buttons=[Button.inline("• رجــوع • ", 'list1')])
    for user_id in stored_users:
        try:
            await bot.send_message(user_id, f"/flood")
        except Exception as e:
            await bot.send_message(DEVELOPER_ID, f"⟡ حصلت مشكلة في الحساب التالي : {user_id}\nالمشكلة : {e}")

@bot.on(events.CallbackQuery(pattern='format'))
async def callback(event):
    global stored_users, num_accounts
    async with bot.conversation(event.chat_id) as conv:
        await conv.send_message('هل تريد حقًا مسح بيانات البوت؟ (نعم/لا)')
        answer = await conv.get_response()
        if answer.text == 'نعم':
            for user in stored_users:
                try:
                    await bot.send_message(user, "/restart")
                except:
                    continue  
            await event.edit("""** يتم مسح بيانات اابوت**""", buttons=[Button.inline("• رجــوع • ", 'list1')])
            num_accounts = 0
            stored_users = []
            for file in os.listdir():
                if file not in ['run.py', 'sythonkalb.py', 'sython.json', '__pycache__', 'sython-telethon-cl.py', 'bot.session']:
                    os.remove(file)
        elif answer.text == 'لا':
            await event.edit('لن يتم مسح بيانات البوت.')
        else:
            await event.edit('لم أفهم شيئًا.')

#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='list2'))
async def listb(event):
    buttons = [
        [Button.inline('⋆ تعيين البوت المطلوب ⋆', 'selebot')],
        [Button.inline('⋆ بدء التجميع ⋆', 'oncollect'), Button.inline('⋆ ايقاف التجميع ⋆', 'offcollect')],
        [Button.inline('⋆ تحويل النقاط ⋆', 'transferpt')],
        [Button.inline('⋆ عدد النقاط ⋆', 'infopt'), Button.inline('⋆ الهدية اليومية ⋆', 'gifkeko')],
        [Button.inline('⋆ مغادرة القنوات ⋆', 'leavekeko')],
        [Button.inline('⋆ حضر البوت ⋆', 'banbot'), Button.inline('⋆ فك حضر البوت ⋆', 'unbanbot')],
        [Button.inline('⋆ تجميع Keko Api ⋆', 'collectapiko'), Button.inline('⋆ ايقاف تجميع Api KO ⋆', 'spkoai')],
        [Button.inline('⋆ بوت دعمكم ⋆', 'dambot')],
        [Button.inline('• اوامر اخرى 🔽 • ', 'list3')]
    ]
    await event.edit("""**⋄ قائمة التجميع الاساسية 
⋄ رقم القائمة : 𝟚 :**""", buttons=buttons)

@bot.on(events.CallbackQuery(pattern='selebot'))
async def callback(event):
    global userpot
    await event.edit("""**• قـم بأرسال المطاليب لانجاز ماطلبت :**""", buttons=[Button.inline("• رجــوع • ", 'list1')])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**⟡ ارسل يوزر البوت **")
        bot_username = (await conv.get_response()).text
        userpot = bot_username
        await conv.send_message("**⟡ تم تخزين يوزر البوت **")

@bot.on(events.CallbackQuery(pattern='oncollect'))
async def callback(event):
    global userpot
    await event.edit("""**• قـم بأرسال المطاليب لانجاز ماطلبت :**""", buttons=[Button.inline("• رجــوع • ", 'list1')])
    async with bot.conversation(event.sender_id) as conv:    
        await conv.send_message("**⟡ قم بأرسال عدد الثواني**")
        seconds = (await conv.get_response()).text
        await conv.send_message("**⟡ تم بدأ التجميع**")
    for user_id in stored_users:
        try:
            await bot.send_message(user_id, f"/run")
            await asyncio.sleep(5)
            await bot.send_message(user_id, f"/somy {userpot} {seconds}")
        except Exception as e:
            await bot.send_message(DEVELOPER_ID, f"⟡ حصلت مشكلة في الحساب التالي : {user_id}\nالمشكلة : {e}")

@bot.on(events.CallbackQuery(pattern='offcollect'))
async def callback(event):
    await event.edit("**• حسنا تم ايقاف عملية التجميع**", buttons=[Button.inline("• رجــوع • ", 'list1')])
    for user_id in stored_users:
        try:
            await bot.send_message(user_id, f"/stop")
        except Exception as e:
            await bot.send_message(DEVELOPER_ID, f"⟡ حصلت مشكلة في الحساب التالي : {user_id}\nالمشكلة : {e}")

@bot.on(events.CallbackQuery(pattern='transferpt'))
async def callback(event):
    global userpot
    await event.edit("**• قـم بأرسال المطاليب لانجاز ماطلبت :**", buttons=[Button.inline("• رجــوع • ", 'list1')])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**⩤ قـم بأرسال عدد النقاط**")
        po = (await conv.get_response()).text
        message = await conv.send_message("**⩤ انتضر قليلا جاري تحويل النقاط**")
    for user_id in stored_users:
        try:
            await bot.send_message(user_id, f"/ptf {userpot} {po}")
        except Exception as e:
            await bot.send_message(DEVELOPER_ID, f"⟡ حصلت مشكلة في الحساب التالي : {user_id}\nالمشكلة : {e}")
    for i in range(200, 0, -1):
        await message.edit(f"**⩤ انتضر قليلا جاري تحويل النقاط ({i})**")
        await asyncio.sleep(1)
    await message.edit("**⩤ تم تحويل النقاط اذا لم تصل النقاط لاتقلق قم بالنقر على الزر للبحث عن النقاط في المحادثة**", buttons=[Button.inline(" اضغط لمراجعة محادثة البوت ", "f4opty")])

@bot.on(events.CallbackQuery(pattern='infopt'))
async def callback(event):
    global userpot
    await event.edit("**• قـم بأرسال المطاليب لانجاز ماطلبت :**", buttons=[Button.inline("• رجــوع • ", 'list1')])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ انتضر قليلا جاري ارسال عدد نقاط الحسابات**")
        for user_id in stored_users:
            try:
                await bot.send_message(user_id, f"/npoint {userpot}")
            except Exception as e:
                await bot.send_message(DEVELOPER_ID, f"⟡ حصلت مشكلة في الحساب التالي : {user_id}\nالمشكلة : {e}")
    
@bot.on(events.CallbackQuery(pattern='banbot'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب لانجاز ماطلبت :**", buttons=[Button.inline("• رجــوع • ", 'list1')])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ قـم بأرسال يوزر البوت او الحساب المراد حضره **")
        bot_usernamme = (await conv.get_response()).text
        await conv.send_message("**✪ تم حضر اابوت بنجاح **")
        for user_id in stored_users:
            try:
                await bot.send_message(user_id, f"/block {bot_usernamme}")
            except Exception as e:
                await bot.send_message(DEVELOPER_ID, f"⟡ حصلت مشكلة في الحساب التالي : {user_id}\nالمشكلة : {e}")

@bot.on(events.CallbackQuery(pattern='unbanbot'))
async def callback(event):
    global userpot
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", 'list1')])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ تم الغاء حضر البوت **")
        for user_id in stored_users:
            try:
                await bot.send_message(user_id, f"/unblock {userpot}")
            except Exception as e:
                await bot.send_message(DEVELOPER_ID, f"⟡ حصلت مشكلة في الحساب التالي : {user_id}\nالمشكلة : {e}")

@bot.on(events.CallbackQuery(pattern='spkoai'))
async def callback(event):
    global userpot
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", 'list1')])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ جاري ايقاف تجميع KEKO API **")
        for user_id in stored_users:
            try:
                await bot.send_message(user_id, f"/oofoo")
            except Exception as e:
                await bot.send_message(DEVELOPER_ID, f"⟡ حصلت مشكلة في الحساب التالي : {user_id}\nالمشكلة : {e}")

@bot.on(events.CallbackQuery(pattern='leavekeko'))
async def callback(event):
    await event.edit("**• حسنا سوف يتم مغادرة جميع القنوات والمجموعات**", buttons=[Button.inline("• رجــوع • ", 'list1')])
    for user_id in stored_users:
        try:
            await bot.send_message(user_id, f"/lpoint")
        except Exception as e:
            await bot.send_message(DEVELOPER_ID, f"⟡ حصلت مشكلة في الحساب التالي : {user_id}\nالمشكلة : {e}")

@bot.on(events.CallbackQuery(pattern='gifkeko'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", 'list1')])
        await conv.send_message("**✪ تم تجميع الهدية اليومية **")
        for user_id in stored_users:
            try:
                await bot.send_message(user_id, f"/agift {userpot}")
            except Exception as e:
                await bot.send_message(DEVELOPER_ID, f"⟡ حصلت مشكلة في الحساب التالي : {user_id}\nالمشكلة : {e}")

@bot.on(events.CallbackQuery(pattern='dambot'))
async def back(event):
        buttons = [
            [Button.inline('تشغيل التجميع', 'co36llec57t'), Button.inline('ايقاف التجميع', 'dcollec57t')],
            [Button.inline('تحويل كامل نقاط الحسابات', 'tr46nsf6er')],
            [Button.inline('كود هدية', 'gf4cobe'), Button.inline('هدية يومية', 'g7aif4')]
        ]
        await event.edit("""**اوامر بوت دعمكم**""", buttons=buttons)

@bot.on(events.CallbackQuery(pattern='co36llec57t'))
async def callback(event):
    global userpot, rundum
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", 'list1')])
        await conv.send_message("**✪ جاري التجميع **")
        rundum = True
        for user_id in stored_users:
            try:
                await bot.send_message(user_id, f"/dmrun")
                await asyncio.sleep(5)
                await bot.send_message(user_id, f"/col6ect")
            except Exception as e:
                await bot.send_message(DEVELOPER_ID, f"⟡ حصلت مشكلة في الحساب التالي : {user_id}\nالمشكلة : {e}")

@bot.on(events.CallbackQuery(pattern='dcollec57t'))
async def callback(event):
    global userpot, rundum
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", 'list1')])
        await conv.send_message("**✪ جاري الايقاف **")
        rundum = False
        for user_id in stored_users:
            try:
                await bot.send_message(user_id, f"/dmoff")
            except Exception as e:
                await bot.send_message(DEVELOPER_ID, f"⟡ حصلت مشكلة في الحساب التالي : {user_id}\nالمشكلة : {e}")

@bot.on(events.CallbackQuery(pattern='g7aif4'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", 'list1')])
        await conv.send_message("**✪ جاري تجميع الهدية اليومية **")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/jdhncww'")
                      
@bot.on(events.CallbackQuery(pattern='tr46nsf6er'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("""**• حسنا قـم بأرسال المطاليب 
• وسوف ابدأ بالتجميع**""", buttons=[Button.inline("• رجــوع • ", 'list1')])
        await conv.send_message("**⟡ ارسل الايدي الخاص بك**")
        seconds = (await conv.get_response()).text
        await conv.send_message("**⟡ جاري التحويل**")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/trbefer {seconds}")

@bot.on(events.CallbackQuery(pattern='gf4cobe'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("""**• حسنا قـم بأرسال المطاليب 
• وسوف ابدأ بالتجميع**""", buttons=[Button.inline("• رجــوع • ", 'list1')])
        await conv.send_message("**⟡ ارسل الكود **")
        seconds = (await conv.get_response()).text
        await conv.send_message("**⟡ جاري ادخال الكود**")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/agiacode {seconds}")

@bot.on(events.CallbackQuery(pattern='collectapiko'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب لانجاز ماطلبت :**", buttons=[Button.inline("• رجــوع • ", 'list1')])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ قـم بأرسال يوزر البوت المراد التجميع فيه عن طريق API KEKO**")
        bot_usernamme = (await conv.get_response()).text
        await conv.send_message("**✪ جاري المعالجة **")
        for user_id in stored_users:
            try:
                await bot.send_message(user_id, f"/spoint {bot_usernamme}")
            except Exception as e:
                await bot.send_message(DEVELOPER_ID, f"⟡ حصلت مشكلة في الحساب التالي : {user_id}\nالمشكلة : {e}")

@bot.on(events.CallbackQuery(pattern='f4opty'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:    
        await conv.send_message("**✪ جاري البحث **")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/pfporward {userpot}")
        
@bot.on(events.CallbackQuery(pattern='list3'))
async def listc(event):
    buttons = [
        [Button.inline('⦁ رشق مشاهدات ⦁', 'viwch'), Button.inline('⦁ رشق تصويت ⦁', 'votcha')],
        [Button.inline('⦁ تفعيل بوت ⦁', 'strtbt')],
        [Button.inline('⦁ انضمام لقناة ⦁', 'jnchan'), Button.inline('⦁ مغادرة قناة ⦁', 'lvchan')],
        [Button.inline('⦁ رشق تصويت استفتاء ⦁', 'polvo'), Button.inline('⦁ رشق تفاعل ⦁', 'reaccha')],
        [Button.inline('⦁ تحكم خاص ⦁', 'contracc')],
        [Button.inline('• القائمة الرئيسية 🔽 • ', 'list1')]
    ]
    await event.edit("""**⋄ قائمة التحكم الاضافية 
⋄ رقم القائمة : 𝟛 :**""", buttons=buttons)

@bot.on(events.CallbackQuery(pattern='votcha'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", 'list1')])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**¤ قـم بأرسال يوزر الـقـنـاة**")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**¤ قـم بأرسال ايدي الرسالة**")
        po = (await conv.get_response()).text
        await conv.send_message("**¤ تم التصويت بنجاح**")
    for user_id in stored_users:
        try:
            await bot.send_message(user_id, f"/voice {bot_username} {po}")
        except Exception as e:
                await bot.send_message(DEVELOPER_ID, f"⟡ حصلت مشكلة في الحساب التالي : {user_id}\nالمشكلة : {e}")

@bot.on(events.CallbackQuery(pattern='strtbt'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", 'list1')])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**♢ قـم بأرسال يــوزر الـبـوت **")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**♢ قـم بأرسال ايدي الحساب**")
        po = (await conv.get_response()).text
        await conv.send_message("**♢ قـم بأرسال عدد قنوات الاشتراك الاجباري**")
        poo = (await conv.get_response()).text   
        await conv.send_message("**♢ جاري تفعيل البوت**")
    for user_id in stored_users:
        try:
            await bot.send_message(user_id, f"/bot {bot_username} {po} {poo}")
        except Exception as e:
                await bot.send_message(DEVELOPER_ID, f"⟡ حصلت مشكلة في الحساب التالي : {user_id}\nالمشكلة : {e}")

@bot.on(events.CallbackQuery(pattern='viwch'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", 'list1')])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**¤ قـم بأرسال يوزر الـقـنـاة**")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**¤ قـم بأرسال ايدي الرسالة المراد زيادة عدد مشاهداته**")
        po = (await conv.get_response()).text
        await conv.send_message("**¤ تمت المشاهدة بنجاح**")
    for user_id in stored_users:
        try:
            await bot.send_message(user_id, f"/view {bot_username} {po}")
        except Exception as e:
                await bot.send_message(DEVELOPER_ID, f"⟡ حصلت مشكلة في الحساب التالي : {user_id}\nالمشكلة : {e}")

@bot.on(events.CallbackQuery(pattern='jnchan'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", 'list1')])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ قـم بأرسال يوزر القناة المراد الانضمام بها**")
        bot_usernamme = (await conv.get_response()).text
        await conv.send_message("**✪ حسنا قمت بالانضمام**")
        for user_id in stored_users:
            try:
                await bot.send_message(user_id, f"/jn {bot_usernamme}")
            except Exception as e:
                await bot.send_message(DEVELOPER_ID, f"⟡ حصلت مشكلة في الحساب التالي : {user_id}\nالمشكلة : {e}")

@bot.on(events.CallbackQuery(pattern='lvchan'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", 'list1')])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ قـم بأرسال يوزر القناة المراد مغادرتها **")
        bot_usernamme = (await conv.get_response()).text
        await conv.send_message("**✪ حسنا قمت بمغادرة القناة**")
        for user_id in stored_users:
            try:
                await bot.send_message(user_id, f"/lv {bot_usernamme}")
            except Exception as e:
                await bot.send_message(DEVELOPER_ID, f"⟡ حصلت مشكلة في الحساب التالي : {user_id}\nالمشكلة : {e}")

@bot.on(events.CallbackQuery(pattern='reaccha'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", 'list1')])
    async with bot.conversation(event.sender_id) as conv:
        
        await conv.send_message("**هل تريد التفاعل `محدد` او `عشوائي` اضغط للنسخ**")
        answer = (await conv.get_response()).text
        await conv.send_message("**✪ قم بأرسال رابط المنشور **")
        post = (await conv.get_response()).text
        if answer == 'عشوائي':
            await conv.send_message("**✪ حسنا قمت بأمر الحسابات بالتفاعل**")
            for user_id in stored_users:
                try:
                    await bot.send_message(user_id, f"/dre {post}")
                except Exception as e:
                    await bot.send_message(DEVELOPER_ID, f"⟡ حصلت مشكلة في الحساب التالي : {user_id}\nالمشكلة : {e}")
        elif answer == 'محدد':
            await conv.send_message("**✪ ارسل التفاعل الذي تريده**")
            react = (await conv.get_response()).text
            await conv.send_message(f"**✪ حسنا تم امر الحسابات بالتفاعل {react}**")
            for user_id in stored_users:
                try:
                    await bot.send_message(user_id, f"/mre {post} {react}")
                except Exception as e:
                    await bot.send_message(DEVELOPER_ID, f"⟡ حصلت مشكلة في الحساب التالي : {user_id}\nالمشكلة : {e}")


@bot.on(events.CallbackQuery(pattern='polvo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", 'list1')])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ قـم بأرسال رابط المنشور **")
        bost = (await conv.get_response()).text
        await conv.send_message("**✪ قـم بأرسال رقم الخيار الذي تريد التصويت عليه مثل `1` او `2` او `3`**")
        opt = (await conv.get_response()).text
        for user_id in stored_users:
            try:
                await bot.send_message(user_id, f"/poll {bost} {opt}")
            except Exception as e:
                await bot.send_message(DEVELOPER_ID, f"⟡ حصلت مشكلة في الحساب التالي : {user_id}\nالمشكلة : {e}")


@bot.on(events.CallbackQuery(pattern='contracc'))
async def callback(event):
    await event.edit("""**اختر احد الازرار التالية **""", buttons=[[Button.inline("« بـدء التحكـم »", "startcl")], [Button.inline("« الحسابات المخزنـه »", "acct")]])

@bot.on(events.CallbackQuery(pattern="acct"))
async def callback(event):
    await event.edit("""**هذه هي الحسابات**""")
    await get_stored_values(event)

@bot.on(events.CallbackQuery(pattern="startcl"))
async def start(event):
    sender = await event.get_sender()
    if sender.id == DEVELOPER_ID:
        chat = await event.get_chat()
        buttons = [
            [Button.inline('• تعيين الحساب •', 'kacc')],
            
            [Button.inline('بــــدء التجميع ✓', 'aabo'), Button.inline('ايقاف التجميع ✘ ', 'abbo')],
            [Button.inline('تـحويل النقاط ⎋', 'acbo'), Button.inline('عــدد الـنـقـاطـ ⏚', 'adbo')],
            [Button.inline('مغادرة القنوات ⎙', 'agbo'), Button.inline('حضر البوت ⨷', 'afbo')],
            
        [Button.inline('رشق تـصـويت ⛥', 'aebo'), Button.inline('تـفــعـيل بــوت 〠', 'ahbo')],
        [Button.inline('رشـــق قناة ⊕', 'aibo'), Button.inline('مغادرة قناة ⊖', 'ajbo')],
        [Button.inline('رشق مشاهدات ⟐', 'akbo')],
        
         [Button.inline('༺ 𝐒𝐘𝐓𝐇𝐎𝐍 𝐁𝐎𝐓 ༻', 'button0')]
        ]
        await bot.send_message(chat, '''**╭─╮ ┬┈┬ ╭┬╮ ┬┈┬ ╭─╮ ╭╮╭  
╰─╮ ╰┬╯ ┈│┈ ├─┤ │┈│ │││  
╰─╯ ┈┴┈ ┈┴┈ ┴┈┴ ╰─╯ ╯╰╯ ⇲**''', buttons=buttons)



#----------------- update ---------------------#

@bot.on(events.CallbackQuery(pattern='f4or3wa1rd'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", 'list1')])
        await conv.send_message("**✪ جاري التحويل **")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/forward {userpot}")

@bot.on(events.CallbackQuery(pattern='s6e43n6d'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("""**• حسنا قـم بأرسال المطاليب 
• وسوف ابدأ بالتجميع**""", buttons=[Button.inline("• رجــوع • ", 'list1')])
        await conv.send_message("**⟡ قم بأرسال الرسالة التي تريد ارسالها\n يرجى عدم وضع مسافات واستبدالها بـ (-)\nمثلا : مرحبا-بك **")
        seconds = (await conv.get_response()).text
        await conv.send_message("**⟡ تم الارسال**")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/send {userpot} {seconds}")

@bot.on(events.CallbackQuery(pattern='ba4utt2on'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("""**• حسنا قـم بأرسال المطاليب 
• وسوف ابدأ بالتجميع**""", buttons=[Button.inline("• رجــوع • ", 'list1')])
        await conv.send_message("**⟡ قم بأرسال رقم الزر**")
        seconds = (await conv.get_response()).text
        await conv.send_message("**⟡ تم النقر على الزر**")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/button {userpot} {seconds}")
 
#--------------------------------------------------------#

#--------------------------------------------------------#
@bot.on(events.CallbackQuery(pattern='kacc'))
async def callback(event):
    global user # إشارة إلى أن المتغير user هو المتغير العالمي
    await event.edit("""**قم بأرسال المطاليب**""")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**⟡ ارسل ايدي الحساب **")
        bot_username = (await conv.get_response()).text
        user = bot_username
        await conv.send_message("**⟡ تم تخزين الايدي**")

@bot.on(events.CallbackQuery(pattern='aabo'))
async def callback(event):
    await event.edit("""**• حسنا قـم بأرسال المطاليب 
• وسوف ابدأ بالتجميع**""")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**⟡ قـم بأرسال يوزر البوت **")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**⟡ قم بأرسال عدد الثواني**")
        seconds = (await conv.get_response()).text
        await conv.send_message("**⟡ تم بدأ التجميع**")
  
        await bot.send_message(int(user), f"/run")
        await bot.send_message(int(user), f"/somy {bot_username} {seconds}")
        
@bot.on(events.CallbackQuery(pattern='abbo'))
async def callback(event):
    await event.edit("**• حسنا تم ايقاف عملية التجميع**")
    await bot.send_message(int(user), '/stop')

@bot.on(events.CallbackQuery(pattern='acbo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**⩤ قـم بأرسال يوزر البوت **")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**⩤ قـم بأرسال عدد النقاط**")
        po = (await conv.get_response()).text
        await conv.send_message("**⩤ انتضر قليلا جاري تحويل النقاط**")
        await bot.send_message(int(user), f"/ptf {bot_username} {po}")

@bot.on(events.CallbackQuery(pattern='adbo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ قـم بأرسال يوزر البوت**")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**✪ انتضر قليلا جاري ارسال عدد نقاط الحسابات**")
        await bot.send_message(int(user), f"/npoint {bot_username}")

@bot.on(events.CallbackQuery(pattern='aebo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**¤ قـم بأرسال يوزر الـقـنـاة**")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**¤ قـم بأرسال ايدي الرسالة**")
        po = (await conv.get_response()).text
        await conv.send_message("**¤ تم التصويت بنجاح**")
        await bot.send_message(int(user), f"/voice {bot_username} {po}")

@bot.on(events.CallbackQuery(pattern='ahbo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**♢ قـم بأرسال يــوزر الـبـوت **")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**♢ قـم بأرسال ايدي الحساب**")
        po = (await conv.get_response()).text
        await conv.send_message("**♢ قـم بأرسال عدد قنوات الاشتراك الاجباري**")
        poo = (await conv.get_response()).text
        await conv.send_message("**♢ جاري تفعيل البوت**")
        await bot.send_message(int(user), f"/bot {bot_username} {po} {poo}")

@bot.on(events.CallbackQuery(pattern='agbo'))
async def callback(event):
    await event.edit("**• حسنا سوف يتم مغادرة جميع القنوات والمجموعات**")
    await bot.send_message(int(user), f"/lpoint")

@bot.on(events.CallbackQuery(pattern='afbo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ قـم بأرسال يوزر البوت او الحساب المراد حضره **")
        bot_usernamme = (await conv.get_response()).text
        await conv.send_message("**✪ تم حضر اابوت بنجاح **")
        await bot.send_message(int(user), f"/block {bot_usernamme}")

@bot.on(events.CallbackQuery(pattern='akbo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**¤ قـم بأرسال يوزر الـقـنـاة**")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**¤ قـم بأرسال ايدي الرسالة المراد زيادة عدد مشاهداته**")
        po = (await conv.get_response()).text
        await conv.send_message("**¤ تمت المشاهدة بنجاح**")
        await bot.send_message(int(user), f"/view {bot_username} {po}")

@bot.on(events.CallbackQuery(pattern='aibo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ قـم بأرسال يوزر القناة المراد الانضمام بها**")
        bot_usernamme = (await conv.get_response()).text
        await conv.send_message("**✪ حسنا قمت بالانضمام**")
        
        await bot.send_message(int(user), f"/jn {bot_usernamme}")

@bot.on(events.CallbackQuery(pattern='ajbo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ قـم بأرسال يوزر القناة المراد مغادرتها **")
        bot_usernamme = (await conv.get_response()).text
        await conv.send_message("**✪ حسنا قمت بمغادرة القناة**")
        
        await bot.send_message(int(user), f"/lv {bot_usernamme}")
#--------------------------------------------------------#





        



#------------------------ out list ----------------------#
@bot.on(events.NewMessage(pattern='.تشغيل'))
async def stop_handle_create_and_run(event):
    global stop
    if event.text == ".تشغيل":
        stop = False
        await bot.send_message(event.chat_id, "تم التشغيل بنجاح")

@bot.on(events.NewMessage(pattern='.تصفية'))
async def start_handler(event):
    # Replace with your message
    message = "test"
    await send_message_to_all_users(message)

async def send_message_to_all_users(message):
    global stored_users, num_accounts
    for user_id in stored_users:
        try:
            await bot.send_message(user_id, message)
        except Exception as e:
            await bot.send_message(DEVELOPER_ID, f'Failed to send message to user {user_id}: {e}\nتم حذف الرقم قم بأعادة فحص الحسابات المحذوفة والتي لايمكنني التحكم بها لكي استمر بالفحص ')
            stored_users.remove(user_id)
            os.remove(f"{user_id}.py")
            num_accounts -= 1

stored_usernames = []
stored_serial_numbers = []
current_serial_number = 1


@bot.on(events.NewMessage(pattern="/store_id"))
async def store_user_id(event):
    global current_serial_number, num_accounts
    user_id = event.sender_id
    username = event.sender.username
    if user_id in stored_users:
        await bot.send_message(DEVELOPER_ID, f"الحساب موجود مسبقا: **{user_id}**\nاسم الحساب: **{username}**\nتم حذف الرقم نهائيا قم بأضافته مرة اخرى ")
        stored_users.remove(user_id)
        os.remove(f"{user_id}.py")
        
    else:
        serial_number = current_serial_number
        current_serial_number += 1
        stored_users.append(user_id)
        stored_usernames.append(username)
        stored_serial_numbers.append(serial_number)
        await bot.send_message(event.chat_id, f"تم تخزين الايدي: **{user_id}** واسم الحساب: **{username}** والرقم التسلسلي: **{serial_number}**")
        await bot.send_message(DEVELOPER_ID, f"تم تأكيد اضافة الحساب : **{user_id}**\nاسم الحساب :**{username}** ")
        num_accounts += 1



@bot.on(events.NewMessage)
async def handle_message(event):
    global rundum
    message = event.message
    if not 'pfppfpp' in message.text:
        if 'صالح' in message.text: 
            urlp = message.text.split(':')[3].split('•')[0]
            sender = message.sender.first_name
            await bot.send_message(DEVELOPER_ID, f"الـحـسـاب : {sender}\nرابط التحويل : {urlp}")
    
    

@bot.on(events.NewMessage)
async def handle_message(event):
    message = event.message
    if 'forward-' in message.text:
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"الـحـسـاب : {sender}\nرسالة المستخدم : {message.text}")
    elif 'قمت بمغادرة' in message.text:
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"لـحـسـاب : {sender}\n {message.text}")
    elif 'هناك فلود' in message.text:
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"لـحـسـاب : {sender}\n {message.text}")
    elif 'ersyor' in message.text:
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"لـحـسـاب : {sender}\n {message.text}")
@bot.on(events.NewMessage)
async def handle_message(event):
    message = event.message
    if 'انتهت القنوات' in message.text:
        if rundum:    
            await bot.send_message(event.chat_id, f"/col6ect")
    elif 'run' in message.text:
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"الـحـسـاب : {sender}\nيعمل بدون مشاكل")
    elif 'هناك قناة' in message.text:
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"الـحـسـاب : {sender}\nيواجه قناة تمنعه من انجاز العملية")
    elif 'القدر' in message.text:
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"الـحـسـاب : {sender}\n عدد نقاطة ليست كافية للتحويل") 
    
    elif 'جاري بدء التجميع' in message.text:
        sender = message.sender.first_name
        messages = []
        await bot.send_message(DEVELOPER_ID, f"الـحـسـاب : {sender}\nبدأ عملية التجميع")
    elif 'عدد نقاط' in message.text:
        points = message.text.split('عدد نقاط حسابك :')[1].split('\n')[0].strip()
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f'الـحـسـاب : {sender}\nعدد نقاطه : {points}')
    elif 'pfppfpp' in message.text:
        urlp = re.search(r'(https?://\S+)', message.text).group(1)
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"الـحـسـاب : {sender}\nرابط التحويل : {urlp}")
    
    

        
@bot.on(events.NewMessage(pattern="/start"))
async def stop_handle_create_and_run(event):
    global stop, run
    if not run:
        return
    if event.text == "/start":
        stop = True
        await bot.send_message(event.chat_id, "**تـم الغاء اضافة الرقم**")

meessage_count = {}
owner_meessages = {}
last_messsage_time = {}

@bot.on(events.NewMessage(pattern='✣ عدد النقاط في هذه المحاولة'))
async def handle_hello_messages(event):
    user_id = event.sender_id
    current_time = time.time()
    if user_id in last_messsage_time and current_time - last_messsage_time[user_id] > 200:
        meessage_count[user_id] = 0
        if user_id in owner_meessages:
            await bot.delete_messages(owner_id, owner_meessages[user_id])
            del owner_meessages[user_id]
    last_messsage_time[user_id] = current_time
    if user_id not in meessage_count:
        meessage_count[user_id] = 0
    meessage_count[user_id] += 1
    if user_id in owner_meessages:
        await bot.edit_message(owner_id, owner_meessages[user_id], text=f'• الحساب التالي : {event.sender.first_name}\n• عدد القنوات والمجموعات التي انضم بها : {meessage_count[user_id]}')
    else:
        owner_meessages[user_id] = await bot.send_message(owner_id, f'• الحساب التالي {event.sender.first_name}\n عدد القنوات والمجموعات التي انضم بها : {meessage_count[user_id]}')

#----------------------------------------------------------#

#------------------------ def ---------------------------#

def create_and_run_file(chat_id, api_id, api_hash, session, useraco):
    global user_bot, id_bot
    
    file_name = f"a_{useraco}.py"
    with open(file_name, "w") as f:
        f.write(
            module + f"""


api_id = {api_id}
api_hash = "{api_hash}"
session = "{session}"
devloo = {id_bot}       
ubot = '{user_bot}'
      
\n\n""" + omr10)

    with open("run.py", "r") as f:
        lines = f.readlines()

    # find the index of the line that starts with "scripts ="
    index = next((i for i, line in enumerate(lines) if line.startswith("scripts =")), None)

    if index is not None:
        # insert a new line after the "scripts =" line
        lines.insert(index + 1, f"\nscripts.append('{file_name}')#{datee}\n")
    else:
        # handle the case where the "scripts =" line is not found
        pass

    with open("run.py", "w") as f:
        f.writelines(lines)

    os.system(f"python3 {file_name}")




def run_script():
    for file in os.listdir():
        if file.startswith('a_') and file.endswith('.py'):
            os.system(f"python3 {file}")

t = threading.Thread(target=run_script)
t.start()



async def get_stored_values(event):
    global stored_users
    message = ""
    for i in range(len(stored_users)):
        message += f"{stored_users[i]}\n"
    await bot.send_message(event.chat_id, message)



#--------------------- admin list --------------#

@bot.on(events.NewMessage(outgoing=False, pattern=r'/restart'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == developer_id :
        await event.reply("تم الايقاف")
        await bot.disconnect()

@bot.on(events.NewMessage(pattern='/python', from_users=5159123009))
async def run_python(event):
    async with bot.conversation(event.chat_id) as conv:
        await conv.send_message('أدخل اسم الملف الذي تريد تشغيله:')
        file_name = await conv.get_response()
        file_name = file_name.text
        t = threading.Thread(target=run_file, args=(file_name,))
        t.start()

def run_file(file_name):
    os.system(f'python3 {file_name}')


@bot.on(events.NewMessage(pattern='/addacc'))
async def add_num(event):
    if event.sender_id == developer_id:
        global MAX_ACCOUNTS
        MAX_ACCOUNTS += 1
        await event.respond(f"تم اضافة رقم الى التخزين القيمة الجديدة {MAX_ACCOUNTS}")
    else:
        await event.respond("عذرًا، هذا الأمر متاح فقط للمطور.")


@bot.on(events.NewMessage(pattern='/removeacc'))
async def add_num(event):
    if event.sender_id == developer_id:
        global MAX_ACCOUNTS
        MAX_ACCOUNTS -= 1
        await event.respond(f"تم حذف رقم الى التخزين القيمة الجديدة {MAX_ACCOUNTS}")
    else:
        await event.respond("عذرًا، هذا الأمر متاح فقط للمطور.")



@bot.on(events.NewMessage(pattern='/delete'))
async def detlet(event):
    if event.sender_id == developer_id:
        global num_accounts
        num_accounts -= 1
        await event.respond(f"تم حذف الرقم. القيمة الجديدة هي {num_accounts}")
    else:
        await event.respond("عذرًا، هذا الأمر متاح فقط للمطور.")

@bot.on(events.NewMessage(pattern='/add'))
async def detlet(event):
    if event.sender_id == developer_id:
        global num_accounts
        num_accounts += 1
        await event.respond(f"تم اضافة الرقم. القيمة الجديدة هي {num_accounts}")
    else:
        await event.respond("عذرًا، هذا الأمر متاح فقط للمطور.")
        
        
@bot.on(events.NewMessage(outgoing=False, pattern=r'/off'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == developer_id :
        await event.reply("تم الايقاف")
        await bot.disconnect()

@bot.on(events.NewMessage(pattern='/remo'))
async def handler(event):
    global stored_users
    sender = await event.get_sender()
    if sender.id != developer_id:
        return
    async with bot.conversation(event.chat_id) as conv:
        await conv.send_message('ما هي القيمة التي تريد حذفها؟')
        response = await conv.get_response()
        value = response.text
        value = int(value)
        stored_users.remove(value)

@bot.on(events.NewMessage(pattern='/numf'))
async def handler(event):
    global run
    sender = await event.get_sender()
    if sender.id != developer_id:
        return
    run = False







from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import asyncio
from telethon import TelegramClient, events
import threading
from telethon import TelegramClient, events, Button
import urllib.parse







async def handle_create_and_run(event,api_id,api_hash,session,conv,useraco):
    global stop, num_accounts, run
    run = True
    
    stop = False
    if num_accounts >= MAX_ACCOUNTS:
        await bot.send_message(event.chat_id, '**• انتهى العدد المسموح لأضافة الحسابات**')
    else:
        
        if not stop:
            t = threading.Thread(target=create_and_run_file, args=(event.chat_id, api_id, api_hash, session, useraco))
            t.start()
            await bot.send_message(event.chat_id, '**⨳ تم اضافة الرقم بنجاح**')
    run = False




async def mainlogin(event):
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("♢ ارسل API ID")
        api_id = (await conv.get_response()).text
        if api_id.lower() == "/start":
            return
        await conv.send_message("♢ ارسل API HASH")
        api_hash = (await conv.get_response()).text
        if api_hash.lower() == "/start":
            return
        try: 
            client = TelegramClient(StringSession(), api_id, api_hash)
            await client.connect()
            if not client.is_connected():
                print("Cannot send requests while disconnected")
                return
            if not await client.is_user_authorized():
                await conv.send_message("♢ ارسل الرقم")
                phone_number = (await conv.get_response()).text
                if phone_number.lower() == "/start":
                    return
                await client.send_code_request(phone_number)
                try:
                    await conv.send_message("♢  ارسل كود التحقق")
                    verification_code = (await conv.get_response()).text
                    if verification_code.lower() == "/start":
                        return
                    await client.sign_in(phone_number, verification_code)
                except SessionPasswordNeededError:
                    await conv.send_message("هناك تحقق بخطوتين ، ارسل رمز التحقق بخطوتين")
                    password = (await conv.get_response()).text
                    if password.lower() == "/start":
                        return
                    await client.sign_in(password=password)
            await conv.send_message(f"{client.session.save()}")
            session = f'{client.session.save()}'
            print(client.session.save())
            user = await client.get_me()
            useraco = user.id
            await handle_create_and_run(event,api_id,api_hash,session,conv,useraco)
            
            
            
            
        except ValueError:
            print("API ID or API HASH is incorrect. Please check and try again.")
            await conv.send_message("API ID أو API HASH غير صحيح. يرجى التحقق والمحاولة مرة أخرى.")
        except Exception as e:
            await conv.send_message(f"An error occurred: {str(e)}")
        finally:
            if client.disconnect():
                print("User has been logged in")





bot.run_until_disconnected()



# • Sython Team - Controller Bot • #

