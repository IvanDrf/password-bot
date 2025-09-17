from aiogram.fsm.state import State, StatesGroup


class LengthStates(StatesGroup):
    '''Waiting for a message about password length'''
    waiting_length: State = State()


class MatchStates(StatesGroup):
    '''
    Waiting for a message to bind the password
    '''
    waiting_match: State = State()
