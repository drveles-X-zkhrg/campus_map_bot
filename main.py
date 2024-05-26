import asyncio
import logging
import sys
from dotenv import dotenv_values
from typing import List

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton
from keyboards import defualt_kb, friends_kb #
from states import FriendsStatesGroup
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

TOKEN = dotenv_values('.env').get('API_TOKEN')

dp = Dispatcher()


@dp.message(StateFilter(None), CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
    await state.set_state(FriendsStatesGroup.main)

# стейты можно добавить
@dp.message(StateFilter(FriendsStatesGroup.main))
async def echo_handler(message: Message, state: FSMContext) -> None:
    try:
        await message.answer("Список твоих друзей эт кампус:", reply_markup=defualt_kb)
        # тут должен быть вообще вызов апишки
        await state.set_state(FriendsStatesGroup.choose_operation_with_friends)
    except TypeError:
        await message.answer("поломка типа")


@dp.message(StateFilter(FriendsStatesGroup.choose_operation_with_friends))
async def edit_freiends_list(message: Message) -> None:
    try:
        # s = getFriendsFromBd условно
        # s = getCountFriends()
        # если список друзей размер 0 то выводим одну кнопку добавить друга
        await message.answer("cerf", reply_markup=friends_kb)
        # тут должен быть вообще вызов апишки
    except TypeError:
        await message.answer("поломка типа")


@dp.message(StateFilter(FriendsStatesGroup.delete_friends))
async def delete_friends(message: Message, state: FSMContext) -> None:
    try:
        # s = getFriendsFromBd условно
        s = [ 
            'jenniffr@student.21-school.ru',
            'kalynkei@student.21-school.ru', 
            'rachelsa@student.21-school.ru',
            'shandych@student.21-school.ru'
        ]
        # если список друзей размер 0 то выводим одну кнопку добавить друга
        await message.answer("cerf", reply_markup=friends_kb)
        # тут должен быть вообще вызов апишки
    except TypeError:
        await message.answer("поломка типа")    


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    asyncio.run(main())

# при сообщении старт делаем проверку бд


# # новый импорт
# from aiogram.utils.keyboard import InlineKeyboardBuilder

# @dp.message(Command("inline_url"))
# async def cmd_inline_url(message: types.Message, bot: Bot):
#     builder = InlineKeyboardBuilder()
#     builder.row(types.InlineKeyboardButton(
#         text="GitHub", url="https://github.com")
#     )
#     builder.row(types.InlineKeyboardButton(
#         text="Оф. канал Telegram",
#         url="tg://resolve?domain=telegram")
#     )

#     # Чтобы иметь возможность показать ID-кнопку,
#     # У юзера должен быть False флаг has_private_forwards
#     user_id = 1234567890
#     chat_info = await bot.get_chat(user_id)
#     if not chat_info.has_private_forwards:
#         builder.row(types.InlineKeyboardButton(
#             text="Какой-то пользователь",
#             url=f"tg://user?id={user_id}")
#         )

#     await message.answer(
#         'Выберите ссылку',
#         reply_markup=builder.as_markup(),
#     )


def build_list_markup(l: List) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    for i in range(len(l)):
        builder.row(InlineKeyboardButton(
            text=l[i]
        ))

    return builder
