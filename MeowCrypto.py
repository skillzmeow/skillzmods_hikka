__version__ = (0, 0, 2)

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
import requests


class MeowCryptoManagerMod(loader.Module):
    """Perfectly crypto manager"""

    strings = {
        "name": "MeowCrypto",
        "bid_rate": "bid rate",
        "inc_args": "<b>🐳 Incorrect args</b>",
    }
    strings_ru = {
        "bid_rate": "ст. по цене покупки",
        "inc_args": "<b>🐳 Неккоректные аргументы</b>",
    }

    async def cryptocmd(self, message: Message):
        "shows a coins price, use int or float numbers."
        args = utils.get_args_raw(message)
        api_btc = requests.get("https://www.blockchain.com/ru/ticker").json()
        api_privat = requests.get(
            "https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11"
        ).json()
        try:
            if not args:
                args = 0
            fargs = float(args)
            if not args:
                fargs = 1
            form = (
                "💸 <b>{} BITCOIN</b> <em>({})</em>\n"
                "🇺🇸 <code>{}$</code>\n"
                "🇷🇺 <code>{}₽</code>\n"
                "🇺🇦 <code>{}₴</code>\n"
            ).format(
                round(fargs, 10),
                self.strings("bid_rate"),
                round(api_btc["USD"]["buy"] * fargs, 2),
                round(api_btc["RUB"]["buy"] * fargs, 2),
                round(float(api_privat[1]["buy"]) * api_btc["USD"]["buy"] * fargs, 2),
            )
            await utils.answer(message, form)
        except ValueError:
            await utils.answer(message, self.strings("inc_args"))
