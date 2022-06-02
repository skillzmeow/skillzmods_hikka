__version__ = (2, 0, 0)
# module by:
# █▀ █▄▀ █ █░░ █░░ ▀█
# ▄█ █░█ █ █▄▄ █▄▄ █▄

# █▀▄▀█ █▀▀ █▀█ █░█░█
# █░▀░█ ██▄ █▄█ ▀▄▀▄▀
# you can edit this module
# 2022

# requires: pytz
# scope: hikka_only
# meta developer: @skillzmeow
# 

import logging

from .. import loader, utils, main

from ..inline.types import InlineCall
from ..inline.types import InlineQuery
from telethon.tl.types import Message

import random

import datetime
import pytz

from pytz import timezone

logger = logging.getLogger(__name__)

class MyTimeMod(loader.Module):
    """Чючют крутой модуль"""
    
    strings = {
        "name": "MyTime",
        "time": "📡 Accuracy time",
        "cancel_btn": "🚫 Close",
        "back_btn": "⏪ Back",
        "datendtime": "📆 DateTime",
        "timezone": "🌞 All timezones",
        "datecalc": "🧑‍💻 DateCalculator",
        "date": "📆 Date",
        "open_manager": "📓 Open manager",
        "expected_date": "😀 Expected date",
        "ss": "{} days, {} hours, {} minutes.",
        "wyc": "What you choose?😅",
    }
    strings_ru = {
        "time": "📡 Точное время",
        "cancel_btn": "🚫 Закрыть",
        "back_btn": "⏪ Назад",
        "datendtime": "📆 Дата и время",
        "timezone": "🌞 Все таймзоны",
        "datecalc": "🧑‍💻 Счётчик дат",
        "date": "📆 Дата",
        "open_manager": "📓 Открыть менеджер",
        "expected_date": "😀 Ожидаемая дата",
        "ss": "{} дней, {} часов, {} минут.",
        "wyc": "Что выберешь?😅",
    }
    strings_ua = {
        "time": "📡 Точний час",
        "cancel_btn": "🚫 Зачинити",
        "back_btn": "⏪ Назад",
        "datendtime": "📆 Дата і час",
        "timezone": "🌞 Всі таймзони",
        "datecalc": "🧑‍💻 Лічільник дат",
        "date": "📆 Дата",
        "open_manager": "📓 Відкрити менеджер",
        "expected_date": "😀 Очікувана дата",
        "ss": "{} днів, {} годин, {} хвилин",
        "wyc": "Що вибереш?😅",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "expected_date",
                "2023, 1, 1",
                lambda: "Укажите дату ЧЕРЕЗ запятую (year, month, day)",
            ),
            loader.ConfigValue(
                "datetext",
                "🎄 До нового года осталось",
                lambda: "Укажите текст для для вашей даты (До моего дня рождения осталось, и тд)",
            ),
            loader.ConfigValue(
            	"correct_time",
            	"Europe/Moscow",
            	lambda: "To check all timezones use:\n.e import pytz\npytz.all_timezones",
            ),
        )

    @staticmethod
    async def cancel(call: InlineCall):
        await call.delete()
    
    @loader.unrestricted
    async def mytimecmd(self, message: Message):
        """
            
        Command manager
        """
        list = ["модуль от скиллза", "в хикке только кнопочки и смайлики...", "че за хрень?", "хочу фтг", "ваша сессия спижжена скилзом"]
        hz = random.choice(list)
        args = utils.get_args_raw(message)
        if not args:
            await self.inline.form(
                message=message,
                
                text=f'<b>{hz}</b>',
                
                reply_markup=[
                    [
                        {
                            "text": self.strings("open_manager"),
                            "callback": self.back_btn,
                        },
                    ],
                ],
            )
        else:
        	await utils.answer(message, "эм чо хочещ")
            
    async def time_call(self, call: InlineCall) -> None:
    	
        tz = timezone(self.config["correct_time"])
        timenow = datetime.datetime.now(tz)
        time = timenow.strftime("%H:%M:%S")
        date = timenow.strftime("%d.%m.%Y")
        
        await call.edit(
        	
            text=f"\n<b>{self.strings('date')}: {date}\n\n{self.strings('time')}: {time}</b>",
            
            reply_markup=[
                [
                    {
                        "text": self.strings("back_btn"),
                        "callback": self.back_btn,
                    },
                    {
                        "text": self.strings("cancel_btn"),
                        "callback": self.cancel
                    },
                ],
            ],
        )

    async def expectedtime_call(self, call: InlineCall):
        stroka = str(self.config["expected_date"])
        tz = timezone(self.config["correct_time"])
        timenow = datetime.datetime.now(tz)
        n = datetime.datetime(*self.config["expected_date"], tzinfo=tz)
        d = n - timenow
        mm = divmod(d.seconds, 60)[0]
        hh, mm = divmod(mm, 60)
        await call.edit(
        	
        	text=f"<b><u>{self.strings('datecalc')}</u>\n\n{self.config['datetext']}:</b> <code>{self.strings('ss').format(d.days, hh, mm)}</code>",
        	
        	reply_markup=[
        		[
        			{
        				"text": self.strings("back_btn"),
        				"callback": self.back_btn,
        			},
        			{
        				"text": self.strings("cancel_btn"),
        				"callback": self.cancel,
        			},
        		],
        	],
        )
    def _get_mark(self):
        return (
            {"text": "больше модулей здесь", "url": "https://t.me/smeowcodes"}
        )

    async def timezonescmd(self, message: Message):
    	await self.inline.form(
    		message=message,
    		text="Timezones",
    		reply_markup=self._get_mark(),
    		**(
                {"photo": "https://0x0.st/oBvb.jpg"}
            ),
    	)
    async def back_btn(self, call: InlineCall):
    	await call.edit(
    		text=f"<b>{self.strings('wyc')}</b>",
            reply_markup=[
                [
                    {
                        "text": self.strings("datendtime"),
                        "callback": self.time_call,
                    },
                    {
                        "text": self.strings("datecalc"),
                        "callback": self.expectedtime_call,
                    },
                ],
                [{"text": self.strings("cancel_btn"), "callback": self.cancel}],
            ],
        )