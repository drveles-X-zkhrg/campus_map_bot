"""Telegram bot entry point for campus map friend tracking."""

import asyncio
import logging
import os
import sys
from datetime import datetime, timedelta, timezone
from typing import List

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from api_calls import (
    add_friend,
    delete_friend,
    get_friends,
    get_friends_status,
    get_peer_status,
)
from keyboards import (
    get_back_keyboard,
    get_friends_list_to_delete_keyboard,
    get_main_keyboard,
)
from states import FriendsStatesGroup

TOKEN = os.getenv("BOT_API_TOKEN", "NotDefined")
MOSCOW_TZ = timezone(timedelta(hours=3))

dp = Dispatcher()


def _current_timestamp() -> str:
    """Return the current Moscow time formatted for bot messages."""
    return datetime.now(tz=MOSCOW_TZ).strftime("%Y-%m-%d %H:%M")


def make_answer_list_friends(friends: List[str]) -> str:
    """Build the prompt shown when adding a new friend."""
    return "Write nickname to add. Now on the friends list:\n" + "\n".join(friends)


@dp.message(CommandStart())
async def start_command_handler(message: Message, state: FSMContext) -> None:
    """Handle /start and show the current friends status."""
    await state.set_state(None)
    try:
        status_message = get_friends_status(message.from_user.id)
        await message.answer(
            f"{_current_timestamp()}\n{status_message}",
            reply_markup=get_main_keyboard(),
        )
    except TypeError:
        await message.answer("error at start_command_handler()")


@dp.callback_query(F.data == "act_start")
async def start_callback_handler(callback: CallbackQuery, state: FSMContext) -> None:
    """Return to the main screen from an inline keyboard action."""
    await state.set_state(None)
    try:
        status_message = get_friends_status(callback.from_user.id)
        await callback.answer()
        await callback.message.edit_text(
            f"{_current_timestamp()}\n{status_message}",
            reply_markup=get_main_keyboard(),
        )
    except TypeError:
        await callback.message.edit_text("error at start_callback_handler()")


@dp.callback_query(F.data == "act_refresh")
async def refresh_callback_handler(
    callback: CallbackQuery, state: FSMContext
) -> None:
    """Refresh friends status from the inline keyboard."""
    await state.set_state(None)
    try:
        status_message = get_friends_status(callback.from_user.id)
        await callback.answer()
        await callback.message.edit_text(
            f"{_current_timestamp()}\n{status_message}",
            reply_markup=get_main_keyboard(),
        )
        await state.set_state(FriendsStatesGroup.add_friend)
    except TypeError:
        await callback.message.edit_text("error at refresh_callback_handler()")


@dp.message(Command("add"))
async def add_friend_command_handler(message: Message, state: FSMContext) -> None:
    """Handle /add and prompt for a nickname to add."""
    await state.set_state(None)
    try:
        friends = get_friends(message.from_user.id)
        await message.answer(
            make_answer_list_friends(friends),
            reply_markup=get_back_keyboard().as_markup(),
        )
        await state.set_state(FriendsStatesGroup.add_friend)
    except TypeError:
        await message.answer("error at add_friend_command_handler()")


@dp.message(Command("delete"))
async def delete_friend_command_handler(message: Message, state: FSMContext) -> None:
    """Handle /delete and show friends that can be removed."""
    await state.set_state(None)
    try:
        friends = get_friends(message.from_user.id)
        await message.answer(
            "Click on a friend's nickname to delete it.",
            reply_markup=get_friends_list_to_delete_keyboard(friends).as_markup(),
        )
    except TypeError:
        await message.answer("error at delete_friend_command_handler()")


@dp.message(Command("help"))
async def help_command_handler(message: Message, state: FSMContext) -> None:
    """Handle /help and show available bot commands."""
    await state.set_state(None)
    try:
        await message.answer(
            "Write a nickname to see where the person is.\n"
            "/start to see friends' status.\n"
            "/add or ➕ to add new friends to the list.\n"
            "/delete or ➖ to remove friends from the list.\n"
            "🔄 to to update statuses."
        )
    except TypeError:
        await message.answer("error at help_command_handler()")


@dp.callback_query(F.data == "act_add")
async def add_friend_callback_handler(
    callback: CallbackQuery,
    state: FSMContext,
) -> None:
    """Open the add-friend flow from the inline keyboard."""
    await state.set_state(None)
    try:
        friends = get_friends(callback.from_user.id)
        await callback.answer()
        await callback.message.edit_text(
            make_answer_list_friends(friends),
            reply_markup=get_back_keyboard().as_markup(),
        )
        await state.set_state(FriendsStatesGroup.add_friend)
    except TypeError:
        await callback.message.edit_text("error at add_friend_callback_handler()")


@dp.callback_query(F.data == "act_delete")
async def delete_friend_callback_handler(
    callback: CallbackQuery, state: FSMContext
) -> None:
    """Open the delete-friend flow from the inline keyboard."""
    await state.set_state(None)
    try:
        friends = get_friends(callback.from_user.id)
        await callback.answer()
        await callback.message.edit_text(
            "Click on the nickname of the friend you want to delete.",
            reply_markup=get_friends_list_to_delete_keyboard(friends).as_markup(),
        )
    except TypeError:
        await callback.message.answer("error at delete_friend_callback_handler()")


@dp.callback_query(F.data.startswith("delete_"))
async def delete_chosen_friend_callback_handler(
    callback: CallbackQuery, state: FSMContext
) -> None:
    """Delete the friend selected from the inline keyboard."""
    del_person = callback.data.replace("delete_", "")
    delete_friend(callback.from_user.id, del_person)
    friends = get_friends(callback.from_user.id)
    await callback.answer(text=f"{del_person} deleted.", show_alert=True)
    await callback.message.edit_text(
        "Pick a nickname to delete",
        reply_markup=get_friends_list_to_delete_keyboard(friends).as_markup(),
    )
    await state.set_state(None)


@dp.message(FriendsStatesGroup.add_friend)
async def add_friend_commit(message: Message, state: FSMContext) -> None:
    """Persist a nickname entered during the add-friend flow."""
    add_friend(message.from_user.id, message.text.strip().lower()[:10])
    await state.set_state(None)
    await add_friend_command_handler(message=message, state=state)


@dp.message(StateFilter(None))
async def peer_status_handler(message: Message, state: FSMContext) -> None:
    """Look up a peer by nickname when no other state is active."""
    status_message = get_peer_status(message.text.lower().strip())
    await state.set_state(None)
    await message.answer(status_message)


async def main() -> None:
    """Start the Telegram bot polling loop."""
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    asyncio.run(main())
