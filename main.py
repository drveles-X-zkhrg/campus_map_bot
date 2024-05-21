import asyncio
import logging
import sys
from dotenv import dotenv_values

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
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
