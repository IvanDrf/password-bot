from aiogram.fsm.state import State, StatesGroup


class LengthStates(StatesGroup):
    '''Waiting for a message about password length'''
    waiting_length: State = State()


class AssociationStates(StatesGroup):
    '''
    Waiting for a message to bind the password
    '''
    waiting_new_association: State = State()
    waiting_changing_association: State = State()
