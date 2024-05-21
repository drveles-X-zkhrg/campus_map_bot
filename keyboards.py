from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

defualt_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Кнопка"), KeyboardButton(text="Питон")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Че будем делать?"
)

friends_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="добавить"), KeyboardButton(text="удалить"), KeyboardButton(text="назад")]
    ],
    resize_keyboard=True,
    input_field_placeholder="выбирай добавить или удалить"
)