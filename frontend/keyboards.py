"""Inline keyboard builders for the Telegram bot."""

from typing import List

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_main_keyboard() -> InlineKeyboardMarkup:
    """Return the main action keyboard (add, refresh, delete)."""
    buttons = [
        [
            InlineKeyboardButton(text="➕", callback_data="act_add"),
            InlineKeyboardButton(text="🔄", callback_data="act_refresh"),
            InlineKeyboardButton(text="➖", callback_data="act_delete"),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_friends_list_to_delete_keyboard(friends: List[str]) -> InlineKeyboardBuilder:
    """Build a keyboard listing friends that can be deleted."""
    builder = InlineKeyboardBuilder()
    for nickname in friends:
        builder.row(
            InlineKeyboardButton(text=nickname, callback_data=f"delete_{nickname}")
        )

    builder.row(InlineKeyboardButton(text="🔙", callback_data="act_start"))

    return builder


def get_back_keyboard() -> InlineKeyboardBuilder:
    """Build a keyboard with a single back button."""
    builder = InlineKeyboardBuilder()

    builder.row(InlineKeyboardButton(text="🔙", callback_data="act_start"))

    return builder
