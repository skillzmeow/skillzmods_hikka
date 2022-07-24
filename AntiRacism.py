__version__ = (0, 0, 1)

# module by:
# █▀ █▄▀ █ █░░ █░░ ▀█
# ▄█ █░█ █ █▄▄ █▄▄ █▄
#        /\_/\
#       ( o.o )
#        > ^ <
# █▀▄▀█ █▀▀ █▀█ █░█░█
# █░▀░█ ██▄ █▄█ ▀▄▀▄▀
#   you can edit this module
#            2022
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# meta developer: @smeowcodes

from .. import loader, utils
from telethon.tl.types import Message


class AntiRacismMod(loader.Module):
    strings = {"name": "AntiRacism"}

    async def watcher(self, message: Message):
        text = message.text
        word = [
            "негр",
            "негры",
            "негра",
            "негров",
            "негроид",
            "негроиды",
            "негроида",
            "негроидов",
            "нигга",
            "нигги",
            "негрики",
            "негриков",
        ]
        for i in word:
            if i in text:
                await message.delete()
