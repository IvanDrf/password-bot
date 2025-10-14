from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.repo.repo import Repo
from app.state.state import AssociationStates
from utils.encrypter import Encrypter
from utils.parser import MessageParser


class AssociationChanger:
    def __init__(self, repo: Repo, encrypter: Encrypter) -> None:
        self.repo: Repo = repo
        self.encrypter: Encrypter = encrypter

    async def Start_Association_Changing(self, message: Message, state: FSMContext) -> None:
        await state.clear()

        await message.answer('Enter a theme to associate and new password for it')
        await state.set_state(AssociationStates.waiting_changing_association)

    async def Change_Association(self, message: Message, state: FSMContext) -> None:
        if message.from_user is None or message.from_user.username is None:
            await message.answer('Cant find your username')
            return

        try:
            if message.text is None:
                raise ValueError('message is empty')

            user_id: int | None = await self.repo.Find_User_By_Username(message.from_user.username)
            if user_id is None:
                await message.answer(f'Cant find you in database, please enter /start')
                return

            association, password = MessageParser.ParseMessage(message.text)
            encrypted_password: str = self.encrypter.encrypt(
                password.encode()).decode()

            await self.repo.Change_Association_Password(user_id, encrypted_password, association)

            await message.answer(f'Successfully changed your association {association}')
            await state.clear()

        except ValueError as e:
            await message.answer(f'Invalid input, error: {e}')

        except Exception as e:
            await message.answer(f'Error: {e}')
