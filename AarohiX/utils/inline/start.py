from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AarohiX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ [❤‍🔥𝐇𝐄𝐑𝐎❤‍🔥] 🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❣️ʜᴇʟᴩ❣️",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="❤‍🔥sᴇᴛᴛɪɴɢs❤‍🔥", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💖 𝐌𝐘 𝐋𝐈𝐅𝐋𝐈𝐍𝐄 💖", url=f"https://t.me/iamcuteheroin"),
            InlineKeyboardButton(
                text="🥰 MY LOVE [❣️] 🥰", url=f"https://t.me/HeroKiDuniya"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💝ᴍᴀɪɴᴛᴀɪɴᴇʀ[ᴅɪʟ]💝", user_id=OWNER),
            InlineKeyboardButton(
                text="🥰sᴜᴩᴩᴏʀᴛ[ᴀɪᴍ]🥰", url=config.SUPPORT_GROUP
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ [💞ᴅɪʟ💞]🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥺ʜᴇʟᴩ🥺", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💖 𝐌𝐘 𝐋𝐈𝐅𝐋𝐈𝐍𝐄 💖", url=f"https://t.me/iamcuteheroin"),
            InlineKeyboardButton(
                text="🥰 MY LOVE [❣️] 🥰", url=f"https://t.me/HeroKiDuniya"
            ),
        ],
        [
            InlineKeyboardButton(text="💝ᴍᴀɪɴᴛᴀɪɴᴇʀ[ᴅɪʟ]💝", user_id=OWNER),
            InlineKeyboardButton(
                text="🥰sᴜᴩᴩᴏʀᴛ[ᴀɪᴍ]🥰", url=config.SUPPORT_GROUP
            ),
        ],
        [
            InlineKeyboardButton(
                    text="🥺 ᴏᴡɴᴇʀ 🥺", url=f"https://t.me/HONEY_SINGH_121"
                )
        ],
     ]
    return buttons
