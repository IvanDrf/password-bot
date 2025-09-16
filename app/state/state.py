from aiogram.fsm.state import State, StatesGroup


class LengthStates(StatesGroup):
    waiting_length: State = State()
