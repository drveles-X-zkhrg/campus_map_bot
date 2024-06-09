from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio
import logging
import sys
import os
from dotenv import load_dotenv
from typing import List
from aiogram import F
from api_calls import get_friends, add_friend, delete_friend, get_friends_status, get_peer_status

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery, ReplyKeyboardRemove
from keyboards import get_main_keyboard, get_friends_list_to_delete_keyboard, get_back_keyboard
from aiogram.filters import Command
from aiogram.methods.send_message import SendMessage
from aiogram.methods.edit_message_text import EditMessageText
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from states import FriendsStatesGroup

TOKEN = os.getenv('BOT_API_TOKEN', 'NotDefined')

dp = Dispatcher()


def make_answer_list_friends(l: List[str]) -> str:
    return 'Напиши никнейм друга. Ниже приведены люди которые уже есть в списке твоих друзей. Если захочешь прекратить добавлять друзей, нажми кнопку \"🔙\"\n'+'\n'.join(l)


@dp.message(CommandStart())
async def start_command_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(None)
    try:
        m = get_friends_status(message.from_user.id)
        await message.answer(f"Сообщение для зенмныить \n{m}",
                             reply_markup=get_main_keyboard())
    except TypeError:
        await message.answer("поломка типа")


@dp.message(Command('add'))
async def add_friend_command_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(None)
    try:
        s = get_friends(message.from_user.id)
        await message.answer(make_answer_list_friends(s),
                             reply_markup=get_back_keyboard()
                             .as_markup())
        await state.set_state(FriendsStatesGroup.add_friend)
    except TypeError:
        await message.answer("добавить поломка")


@dp.message(Command("delete"))
async def delete_friend_command_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(None)
    try:
        s = get_friends(message.from_user.id)
        await message.answer(
            'Нажми на ник друга, которого хочешь удалить.',
            reply_markup=get_friends_list_to_delete_keyboard(s)
            .as_markup()
        )
    except TypeError:
        await message.answer("поломка типа")


@dp.message(Command('help'))
async def help_command_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(None)
    try:
        await message.answer("не нажимай сюда никогда!")
    except TypeError:
        await message.answer("добавить поломка")


@dp.callback_query(F.data == "act_start")
async def start_callback_handler(callback: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(None)
    try:
        m = get_friends_status(callback.from_user.id)
        await callback.answer()
        await callback.message.edit_text(f"Сообщение для зенмныить \n{m}",
                                         reply_markup=get_main_keyboard())
    except TypeError:
        await callback.message.edit_text("поломка типа")


@dp.callback_query(F.data == "act_add")
async def add_friend_callback_handler(callback: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(None)
    try:
        s = get_friends(callback.from_user.id)
        await callback.answer()
        await callback.message.edit_text(make_answer_list_friends(s),
                                         reply_markup=get_back_keyboard()
                                         .as_markup())
        await state.set_state(FriendsStatesGroup.add_friend)
    except TypeError:
        await callback.message.edit_text("поломка типа")


@dp.callback_query(F.data == "act_delete")
async def delete_friend_callback_handler(callback: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(None)
    try:
        s = get_friends(callback.from_user.id)
        await callback.answer()
        await callback.message.edit_text(
            'Нажми на ник друга, которого хочешь удалить.',
            reply_markup=get_friends_list_to_delete_keyboard(s)
            .as_markup()
        )
    except TypeError:
        await callback.message.answer("поломка типа")


@dp.callback_query(F.data.startswith("delete_"))
async def delete_chosen_friend_callback_handler(callback: CallbackQuery, state: FSMContext):
    del_person = callback.data.replace('delete_', '')
    delete_friend(callback.from_user.id, del_person)
    s = get_friends(callback.from_user.id)
    await callback.answer(
        text=f"{del_person} удален.",
        show_alert=True
    )
    await callback.message.edit_text(
        "выбери кого хочешь удалить",
        reply_markup=get_friends_list_to_delete_keyboard(s)
        .as_markup()
    )
    await state.set_state(None)


@dp.message(FriendsStatesGroup.add_friend)
async def add_friend_commit(message: Message, state: FSMContext):
    add_friend(message.from_user.id, message.text)
    await state.set_state(None)
    await add_friend_command_handler(message=message, state=state)


@dp.message(StateFilter(None))
async def add_friend_commit(message: Message, state: FSMContext):
    m = get_peer_status(message.text.lower().strip())
    await state.set_state(None)
    await message.answer(f"{m}")


@dp.callback_query(F.data == "act_refresh")
async def delete_friend_callback_handler(callback: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(None)
    try:
        m = get_friends_status(callback.from_user.id)
        await callback.answer()
        await callback.message.edit_text(f"Сообщение для зенмныить \n{m}",
                                         reply_markup=get_main_keyboard())
        await state.set_state(FriendsStatesGroup.add_friend)
    except TypeError:
        await callback.message.edit_text("поломка типа")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(
        parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    asyncio.run(main())
