"""FSM state definitions for the Telegram bot."""

from aiogram.fsm.state import State, StatesGroup


class FriendsStatesGroup(StatesGroup):  # pylint: disable=too-few-public-methods
    """States for managing the friends list."""

    add_friend = State()
