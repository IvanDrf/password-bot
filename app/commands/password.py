from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.repo.repo import Repo
from app.state.state import LengthStates
from utils.converter import NumberConverter
from app.password.generator import PasswordGenerator


class PasswordCreator:
    def __init__(self, repo: Repo) -> None:
        self.repo: Repo = repo

    async def Start_Password_Generation(self, message: Message, state: FSMContext) -> None:
        await state.clear()

        await message.answer('Enter password length:')
        await state.set_state(LengthStates.waiting_length)

    async def Generate_Password(self, message: Message, state: FSMContext) -> None:
        try:
            if message.text is None:
                raise ValueError('message is empty')

            length: int = NumberConverter.From_Str_To_Positive_Int(
                message.text)

            password: str = PasswordGenerator.Generate_Password(length)

            await message.answer(f'Your password: {password}')
            await state.clear()
        except ValueError as e:
            await message.answer(f'Invalid input, error: {e}')
