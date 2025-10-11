from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.repo.repo import Repo
from app.state.state import AssociationStates
from utils.encrypter import Encrypter
from utils.converter import MessageParser


class AssociationAdder:
    def __init__(self, repo: Repo, encrypter: Encrypter) -> None:
        self.repo: Repo = repo
        self.encrypter: Encrypter = encrypter

    async def Start_Password_Association(self, message: Message, state: FSMContext) -> None:
        await message.answer('Enter a theme to associate and password with it, for example: github secret_password')
        await state.set_state(AssociationStates.waiting_new_association)

    async def Associate_Password(self, message: Message, state: FSMContext) -> None:
        try:
            if message.from_user is None or message.from_user.username is None:
                raise ValueError('cant find your username')

            if message.text is None:
                raise ValueError('message is empty')

            association, password = MessageParser.ParseMessage(message.text)

            user_id: int | None = await self.repo.Find_User_By_Username(message.from_user.username)
            if user_id is None:
                await message.answer(f'Cant find you in database, please enter /start')
                return

            encrypted_password: str = self.encrypter.encrypt(
                password.encode()).decode()
            await self.repo.Associate_Password(user_id, encrypted_password, association)

            await message.answer(f'Successfully associated your password with {association}')
            await state.clear()

        except ValueError as e:
            await message.answer(f'Invalid input, error: {e}')

        except Exception as e:
            if 'association' in locals():
                association = locals()['association']
                await message.answer(f'You already have association with {association}')
