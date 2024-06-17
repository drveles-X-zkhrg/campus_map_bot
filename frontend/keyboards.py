from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from typing import List


def get_main_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text="➕",
                                 callback_data="act_add"),
            InlineKeyboardButton(text="🔄",
                                 callback_data="act_refresh"),
            InlineKeyboardButton(text="➖",
                                 callback_data="act_delete")
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_friends_list_to_delete_keyboard(l: List[str]) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    for i in range(len(l)):
        builder.row(InlineKeyboardButton(
            text=l[i], callback_data=f"delete_{l[i]}"
        ))

    builder.row(InlineKeyboardButton(
        text="🔙", callback_data=f"act_start"
    ))

    return builder


def get_back_keyboard() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()

    builder.row(InlineKeyboardButton(
        text="🔙", callback_data=f"act_start"
    ))

    return builder
