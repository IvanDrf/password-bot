from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.repo.repo import Repo


class Starter:
    def __init__(self, repo: Repo) -> None:
        self.repo: Repo = repo

    async def Start(self, message: Message, state: FSMContext) -> None:
        await state.clear()

        if message.from_user is None:
            await message.answer(f'Hello, this is Password Generator Bot')
        else:
            if not (message.from_user.username is None):
                try:
                    await self.repo.Add_User(message.from_user.username)
                except:
                    pass

            await message.answer(f'Hello {message.from_user.first_name}, this is Password Generator Bot')
