from aiogram.fsm.state import StatesGroup, State

class FriendsStatesGroup(StatesGroup):
    main = State()
    choose_operation_with_friends = State()
    delete_friends = State()
    add_friends = State()