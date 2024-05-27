from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio
import logging
import sys
from dotenv import dotenv_values
from typing import List
from aiogram import F

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery, ReplyKeyboardRemove
from keyboards import get_main_keyboard, get_friends_list_to_delete_keyboard, get_back_keyboard
from aiogram.filters import Command
from aiogram.methods.send_message import SendMessage
from aiogram.methods.edit_message_text import EditMessageText


TOKEN = dotenv_values('.env').get('API_TOKEN')

dp = Dispatcher()


def make_answer_list_friends(l: List[str]) -> str:
    return 'Напиши никнейм друга. Ниже приведены люди которые уже есть в списке твоих друзей.\n'+'\n'.join(l)


@dp.message(CommandStart())
async def start_command_handler(message: Message) -> None:
    try:
        # s = getFriends()
        await message.answer("Список твоих друзей эт кампус: у вас 0 друзей и 0 онайлг",
                             reply_markup=get_main_keyboard())
    except TypeError:
        await message.answer("поломка типа")


@dp.callback_query(F.data == "act_start")
async def start_callback_handler(callback: CallbackQuery) -> None:
    try:
        # s = getFriends()
        await callback.message.answer("Список твоих друзей эт кампус: у вас 0 друзей и 0 онайлг",
                                      reply_markup=get_main_keyboard())
    except TypeError:
        await callback.message.answer("поломка типа")


@dp.message(Command('add'))
async def add_friend_command_handler(message: Message) -> None:
    try:
        # s = getFriendsFromBd условно
        s = [
            'jenniffr',
            'kalynkei',
            'rachelsa',
            'shandych'
        ]
        # kb = build_list_markup(s)
        await message.answer(make_answer_list_friends(s),
                             reply_markup=get_back_keyboard()
                             .as_markup())
    except TypeError:
        await message.answer("добавить поломка")


@dp.callback_query(F.data == "act_add")
async def add_friend_callback_handler(callback: CallbackQuery) -> None:
    try:
        # s = getFriendsFromBd условно
        s = [
            'jenniffr',
            'kalynkei',
            'rachelsa',
            'shandych'
        ]
        await callback.message.answer(make_answer_list_friends(s),
                                      reply_markup=get_back_keyboard()
                                      .as_markup())
    except TypeError:
        await callback.message.answer("поломка типа")


@dp.message(Command("delete"))
async def delete_friend_command_handler(message: Message) -> None:
    try:
        # s = getFriendsFromBd условно
        s = [
            'jenniffr',
            'kalynkei',
            'rachelsa',
            'shandych'
        ]
        await message.answer(
            'Нажми на ник друга, которого хочешь удалить.',
            reply_markup=get_friends_list_to_delete_keyboard(s)
            .as_markup()
        )
    except TypeError:
        await message.answer("поломка типа")


@dp.callback_query(F.data == "act_delete")
async def delete_friend_callback_handler(callback: CallbackQuery) -> None:
    try:
        # s = getFriendsFromBd условно
        s = [
            'jenniffr',
            'kalynkei',
            'rachelsa',
            'shandych'
        ]
        await callback.message.answer(
            'Нажми на ник друга, которого хочешь удалить.',
            reply_markup=get_friends_list_to_delete_keyboard(s)
            .as_markup()
        )
        # тут должен быть вообще вызов апишки
    except TypeError:
        await callback.message.answer("поломка типа")


@dp.callback_query(F.data.startswith("delete_"))
async def delete_chosen_friend_callback_handler(callback: CallbackQuery):
    del_person = callback.data.replace('delete_', '')
    # delFriendFromBd(del_person) условно
    # s = getFriendsFromBd() условно
    # часть сверху надо выполнить синхронно
    s = [
        'jenniffr',
        'kalynkei',
        'rachelsa',
        'shandych'
    ]
    s.remove(del_person)
    await callback.message.edit_text(
        "выбери кого хочешь удалить",
        reply_markup=get_friends_list_to_delete_keyboard(s)
        .as_markup()
    )
    await callback.answer(
        text=f"{del_person} удален.",
        show_alert=True
    )


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(
        parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    asyncio.run(main())
