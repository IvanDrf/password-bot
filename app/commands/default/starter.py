from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from typing import Final

from app.repo.repo import Repo
from app.errors.errors import UserException


class Starter:
    buttons: Final = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='/start'), KeyboardButton(text='/help')],
        [KeyboardButton(text='/generate'), KeyboardButton(text='/associate')],
        [KeyboardButton(text='/change'), KeyboardButton(text='/del')],
        [KeyboardButton(text='/my'), KeyboardButton(text='/del_all')],
    ])

    def __init__(self, repo: Repo) -> None:
        self.repo: Repo = repo

    async def Start(self, message: Message, state: FSMContext) -> None:
        await state.clear()

        if message.from_user is None:
            await message.answer(f'Hello, this is Password Generator Bot')
            return

        if not (message.from_user.username is None):
            try:
                user_id: int | None = await self.repo.Find_User_By_Username(message.from_user.username)

                if user_id is None:
                    await self.repo.Add_User(message.from_user.username)

                await message.answer(f'Hello {message.from_user.first_name}, this is Password Generator Bot', reply_markup=Starter.buttons)

            except Exception:
                await message.answer(f'Hello {message.from_user.first_name}, this is Password Generator Bot', reply_markup=Starter.buttons)
