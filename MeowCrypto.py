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
import random as r


class MeowCryptoManagerMod(loader.Module):
    """Awesome cryptocurrency viewer"""

    strings = {
        "name": "MeowCrypto",
        "inc_args": "<b>🐳 Incorrect args</b>",
        "keyerror": "🗿 <b>Maybe the coin is not in the site database or you typed the wrong name</b>",
    }
    strings_ru = {
        "inc_args": "<b>🐳 Неккоректные аргументы</b>",
        "keyerror": "🗿 <b>Возможно монеты нету в базе данных сайта, или вы ввели неккоректное название</b>",
    }

    async def cryptocmd(self, message: Message):
        "use .crypto <count (float or int)> <coin name>. defolt is '1 BTC'"
        args = utils.get_args_raw(message)
        if not args:
            args = "1 BTC"

        args_list = args.split(" ")
        try:
            if len(args_list) == 1 and isinstance(float(args_list[0]), float) == True:
                args_list.append("BTC")
        except Exception:
            args_list = ["1", args_list[0]]
        coin = args_list[1].upper()
        api = requests.get(
            f"https://min-api.cryptocompare.com/data/price?fsym={coin}&tsyms=USD,RUB,UAH,KZT"
        ).json()
        smile = "💷 💶 💴 💵".split(" ")
        smiles = r.choice(smile)
        try:
            try:
                count = float(args_list[0])
                form = (
                    "{} <b>{} {}</b>\n"
                    "🇺🇸 <code>{}$</code>\n"
                    "🇷🇺 <code>{}₽</code>\n"
                    "🇺🇦 <code>{}₴</code>\n"
                    "🇰🇿 <code>{}₸</code>"
                ).format(
                    smiles,
                    count,
                    coin,
                    round(api["USD"] * count, 2),
                    round(api["RUB"] * count, 2),
                    round(api["UAH"] * count, 2),
                    round(api["KZT"] * count, 2),
                )
                await utils.answer(message, form)
            except KeyError:
                await utils.answer(message, self.strings("keyerror"))
        except ValueError:
            await utils.answer(message, self.strings("inc_args"))
