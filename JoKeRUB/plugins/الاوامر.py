# WRITE  BY JoKeRUB
# PLUGIN FOR JoKeRUB 
# @ucriss

from telethon import events
import random, re
from ..Config import Config

from JoKeRUB.utils import admin_cmd

import asyncio
from JoKeRUB import l313l
from random import choice

from ..core.managers import edit_or_reply
from ..sql_helper.globals import gvarstatus

plugin_category = "extra"

rehu = [
    "أﻧـჂ̤ ﺑݽہ اسلوبي وضحڪتي تسوا، ﭑنتيہ و؏ـشـيرتك ييروححَي 🐍😂😭.@ucriss",
    "أنا أمرأة اعدل كلُ نساءَ العالمِ بشخصيتي!..@C_0_R_S",
    "اليفكر ياخذني للتسليه اخذه حيوان للتربيه.🐆🔥@ze_in22",
    "ٱࢦيـتݛڪنـﯥ ٱتـݛڪھٰـہ ﯛ ٱتـف ؏ ﯛ جـهـه ✗ ❭😂🚶‍♀😹ٌ",
    "عيونج أخضر من شجرنه💚🕸ه @C_0_R_S",
    "لو #تصيࢪون انبيا۽ هـم #مࢪاحح اعتࢪف بيـڪم 🍷ه",
    "سَاختَصرهَا لهَم بانكَ تخصـَني  . @AlP_MRKK @C_0_R_S",
    "رقيقة الوصف ، وسيده كل الحُسن .@C_0_R_S",
]
@l313l.ar_cmd(pattern="الاوامر(?:\s|$)([\s\S]*)")
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        lMl10l = random.choice(rehu)
        await event.edit(
        f": **⦑ قائمة اوامر ايــڪاࢪ ⦒**\n≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n( `.م1` )  ⦙ **اوامر الادمن**\n( `.م2` )  ⦙ **اوامر المجموعة**\n( `.م3` )  ⦙ **اوامر الترحيب والردود**\n( `.م4` )  ⦙ **حماية خاص والتلكراف**\n( `.م5` )  ⦙ **اوامر المنشن والانتحال**\n( `.م6` )  ⦙ **اوامر التحميل والترجمة**\n( `.م7` )  ⦙ **اوامر المنع و القفل**\n( `.م8` )  ⦙ **اوامر التنظيف والتكرار**\n( `.م9` )  ⦙ **اوامر التخصيص والفارات**\n( `.م10` ) ⦙ **اوامر الوقتي و التشغيل**\n( `.م11` ) ⦙ **اوامر الكشف و الروابط**\n( `.م12` ) ⦙ **اوامر المساعدة والإذاعة** \n( `.م13` ) ⦙ **اوامر الارسال والاذكار**\n( `.م14` ) ⦙ **اوامر المـلصقات وكوكل**\n( `.م15` ) ⦙ **اوامر التسلية والميمز والتحشيش** \n( `.م16` ) ⦙ **اوامر الصيغ والجهات**\n( `.م17` ) ⦙ **اوامر التمبلر والزغرفة والمتحركة**\n( `.م18` ) ⦙ **اوامر الحساب والترفيه**\n( `.م19` ) ⦙ **اوامر الميوزك والتشغيل**\n( `.م20` ) ⦙ **اوامر بصمات الميمز**\n( `.م21` ) ⦙ **اوامر تجميع النقاط وبوت وعد**\n≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n **᯽︙ {lMl10l} **"
)

@l313l.ar_cmd(
    pattern="م1$",
    command=("م1", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الادمن لسورس ايــڪاࢪ **:\n ≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الحظر` )\n- ( `.اوامر الكتم` )\n- ( `.اوامر التثبيت` )\n- ( `.اوامر الاشراف` )\n≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n⌔︙CH : @ucriss"
)
		
@l313l.ar_cmd(
    pattern="م2$",
    command=("م2", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر المجـموعه لسورس ايــڪاࢪ **:\n ≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التفليش` )\n- ( `.اوامر المحذوفين` )\n- ( `.اوامر الكروب` )\n≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n⌔︙CH : @ucriss"
)

@l313l.ar_cmd(
    pattern="م3$",
    command=("م3", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الـترحيب والـردود **:\n ≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الترحيب` )\n- ( `.اوامر الردود` )\n≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n⌔︙CH : @ucriss"
)
@l313l.ar_cmd(
    pattern="م4$",
    command=("م4", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر حـماية الخاص والتلكراف **:\n ≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الحماية` )\n- ( `.اوامر التلكراف` ) \n≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n⌔︙CH : @ucriss"
)
@l313l.ar_cmd(
    pattern="م5$",
    command=("م5", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الـمنشن والانتحال **:\n ≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الانتحال` )\n- ( `.اوامر التقليد` )\n- ( `.اوامر المنشن` ) \n≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n⌔︙CH : @ucriss"
)

@l313l.ar_cmd(
    pattern="م6$",
    command=("م6", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التحميل والترجمه **:\n ≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر النطق` )\n- ( `.اوامر التحميل` )\n- ( `.اوامر الترجمة` ) \n≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n⌔︙CH : @ucriss"
)

@l313l.ar_cmd(
    pattern="م7$",
    command=("م7", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر القفل والمنع **:\n≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر القفل` )\n- ( `.اوامر الفتح` )\n- ( `.اوامر المنع` ) \n≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n⌔︙CH : @ucriss"
)

@l313l.ar_cmd(
    pattern="م8$",
    command=("م8", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التكرار والتنظيف **:\n≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التكرار` )\n- ( `.اوامر السبام` )\n- ( `.اوامر التنظيف` ) \n- ( `.اوامر المسح` ) \n≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n⌔︙CH : @ucriss"
)

@l313l.ar_cmd(
    pattern="م9$",
    command=("م9", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة التخصيص والفارات **:\n ≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التخصيص` )\n لتغير الصور والكلايش كل من الحماية والفحص والبنك\n- ( `.اوامر الفارات` )\n - لتغير الاسم وزخرفة الوقت والصورة الوقتية والمنطقة الزمنية ورمز الاسم والبايو الوقتي وغيرها\n≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n⌔︙CH : @ucriss"
		)

@l313l.ar_cmd(
    pattern="م10$",
    command=("م10", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الوقتي والتشغيل **:\n ≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الاسم` )\n- ( `.اوامر البايو` )\n- ( `.اوامر الكروب الوقتي` )\n- ( `.اوامر التشغيل` ) \n- ( `.اوامر الاطفاء` ) \n≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n⌔︙CH : @ucriss"
)	

@l313l.ar_cmd(
    pattern="م11$",
    command=("م11", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الكـشف و الروابط **:\n ≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الكشف` )\n- ( `.اوامر الروابط` ) \n\n ≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n⌔︙CH : @ucriss"
)
@l313l.ar_cmd(
    pattern="م12$",
    command=("م12", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر المساعدة  **:\n ≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الوقت والتاريخ` )\n- ( `.اوامر كورونا` )\n- ( `.اوامر الصلاة` ) \n- ( `.اوامر مساعدة` )\n- ( `.اوامر الاذاعه` ) \n≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n⌔︙CH : @ucriss"
)
@l313l.ar_cmd(
    pattern="م13$",
    command=("م13", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الارسال **:\n ≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.امر الصورة الذاتية` )\n- ( `.اوامر التحذيرات` )\n- ( `.اوامر اللستة` )\n- ( `.اوامر الملكية` ) \n- ( `.اوامر السليب` ) \n- ( `.اوامر الاذكار` )\n≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n⌔︙CH : @ucriss"
)
@l313l.ar_cmd(
    pattern="م14$",
    command=("م14", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الملصقات وكوكل **:\n ≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الملصقات` )\n- ( `.اوامر كوكل` )\n≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n⌔︙CH : @ucriss"
)

@l313l.ar_cmd(
    pattern="م15$",
    command=("م15", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التسلية والتحشيش **:\n ≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التسلية` )\n- ( `.اوامر التحشيش` )\n- ( `.اوامر الميمز` )\n≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n⌔︙CH : @ucriss"
)

@l313l.ar_cmd(
    pattern="م16$",
    command=("م16", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر تحويل الصيغ و الجهات **:\n ≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التحويل` )\n- ( `.اوامر الجهات` ) \n≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n⌔︙CH : @ucriss"
)

@l313l.ar_cmd(
    pattern="م18$",
    command=("م18", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الحساب و الترفيه **:\n ≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الترفيه` )\n- ( `.اوامر الحساب` ) \n≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n⌔︙CH : @ucriss"

)

@l313l.ar_cmd(
    pattern="م19",
    command=("م19", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        " قائمة اوامر الميوزك والتشغيل 🎵\n ≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n᯽︙ اختر احدى هذه الاوامر\n ᯽︙ قبل أستخدام هذه الاوامر يجب تفعيل المود بكتابة ألامر ( `.ميوزك تفعيل` ) \n- ( `.تشغيل_المكالمة` )\n- لتشغيل المحادثة الصوتيه\n- ( `.انهاء_المكالمة` )\n-لأنهاء المحادثه الصوتية \n- ( `.دعوة` )\n- بالرد على الشخص لدعوته الى المكالمة \n- ( `.معلومات_المكالمة` )\n- لعرض عنوان المكالمة وعدد لاشخاص الموجودين فيها \n- ( `.تسمية_المكالمة` )\n- لتغير عنوان المكالمة \n- ( `.انضمام` )\n- للأنضمام الى المحادثة الصوتية\n- ( `.مغادرة` )\n- لمغادرة المحادثة الصوتية \n- ( `.تشغيل` )\n-بالرد على رابط اليوتيوب او كتابة الامر مع رابط ليوتيوب لتشغيل الاغنيه \n- ( `.قائمة_التشغيل` )\n- لعرض قائمة التشغيل \n- ( `.ايقاف_مؤقت` )\n - لأيقاف الاغنية الحالية مؤقتا \n- ( `.استمرار` )\n -لأستمرار الاغنيه التي تم ايقافها \n- ( `.تخطي` )\n- لتخطي الاغنيه وتشغيل الاغنيه الموجوده في قائمة التشغيل \n\n ≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n⌔︙CH : @ucriss"



)

@l313l.ar_cmd(
    pattern="م20$",
    command=("م20", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر بصمات الميمز **:\n ≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.بصمات ميمز` )\n- ( `.بصمات ميمز2` )\n- ( `.بصمات ميمز3` )\n- ( `.بصمات ميمز4` )\n- ( `.بصمات ميمز5` )\n- ( `.بصمات انمي` ) \n≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n⌔︙CH : @ucriss"

)

@l313l.ar_cmd(
    pattern="م21$",
    command=("م21", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "** قائمة اوامر تجميع النقاط و بوت وعد **:\n ≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التجميع` ) \n- ( `.اوامر وعد` ) \n≪⊶⌯༺ sourCe Ꭵkαᖇ ༻⌯⊷≫\n⌔︙CH : @ucriss"
        )
