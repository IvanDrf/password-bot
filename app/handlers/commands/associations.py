from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.state.state import AssociationStates
from app.repo.repo import Repo
from app.errors.errors import UserException
from app.utils.converter import MessageParser
from app.utils.respondent import Respondent
from app.utils.encrypter import Encrypter
from config.config import Config


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

            user_id: int = await self.repo.Find_User_By_Username(message.from_user.username)

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


class AssociationChanger:
    def __init__(self, repo: Repo, encrypter: Encrypter) -> None:
        self.repo: Repo = repo
        self.encrypter: Encrypter = encrypter

    async def Start_Association_Changing(self, message: Message, state: FSMContext) -> None:
        await message.answer('Enter a theme to associate and new password for it')
        await state.set_state(AssociationStates.waiting_changing_association)

    async def Change_Association(self, message: Message, state: FSMContext) -> None:
        if message.from_user is None or message.from_user.username is None:
            await message.answer('Cant find your username')
            return

        try:
            if message.text is None:
                raise ValueError('message is empty')

            user_id: int = await self.repo.Find_User_By_Username(message.from_user.username)

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


class AssociationDeleter:
    def __init__(self, repo: Repo) -> None:
        self.repo: Repo = repo

    async def Start_Association_Deletion(self, message: Message, state: FSMContext) -> None:
        await message.answer('Enter the association you want to delete, for example: github')
        await state.set_state(AssociationStates.waiting_deletion_association)

    async def Delete_Association(self, message: Message, state: FSMContext) -> None:
        if message.from_user is None or message.from_user.username is None:
            await message.answer('Cant find your username')
            return

        try:
            if message.text is None:
                raise ValueError('message is empty')

            user_id: int = await self.repo.Find_User_By_Username(message.from_user.username)

            await self.repo.Delete_Association(user_id, message.text)

            await message.answer(f'Successfully deleted your association {message.text}')
            await state.clear()
        except ValueError as e:
            await message.answer(f'Invalid input, error: {e}')

        except UserException as e:
            await message.answer(f'Error: {e}')

        except Exception as e:
            await message.answer(f'Cant find your association {message.text}')


class AssociationPrinter:
    def __init__(self, repo: Repo, encrypter: Encrypter) -> None:
        self.repo: Repo = repo
        self.encrypter: Encrypter = encrypter

    async def Print_User_Associations(self, message: Message, state: FSMContext) -> None:
        await state.clear()

        if message.from_user is None or message.from_user.username is None:
            await message.answer('Cant find your username')
            return

        try:
            user_id: int = await self.repo.Find_User_By_Username(message.from_user.username)
            associations: list[list[str]] = await self.repo.Find_Password_Associations(user_id)

            for i in range(len(associations)):
                associations[i][1] = self.encrypter.decrypt(
                    associations[i][1]).decode()

            answer: str = Respondent.Create_Associations_List(
                associations)

            await message.answer(answer)
        except:
            await message.answer('You dont have any associations')
