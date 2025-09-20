from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from typing import Final

from app.password.generator import Generator
from app.state.state import LengthStates, AssociationStates
from app.repo.repo import Repo
from config.config import Config
from app.repo.errors import UserException
from app.utils.converter import NumberConverter, MessageParser
from app.utils.respondent import Respondent


class BotCommands:
    help_command: Final = '''
Commands:
/start - start bot
/help - display the list of available commands
/generate - start generating a new password
/associate - associate word with your password
/change - change password to your association
/my - print your associations
'''

    def __init__(self, repo: Repo) -> None:
        self.repo: Repo = repo

    @classmethod
    async def New(cls, cfg: Config) -> 'BotCommands':
        repo: Repo = await Repo.New(cfg)

        return cls(repo)

    async def Start_Handler(self, message: Message, state: FSMContext) -> None:
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

    async def Help_Handler(self, message: Message, state: FSMContext) -> None:
        await state.clear()

        await message.answer(BotCommands.help_command)

    async def Start_Password_Generation(self, message: Message, state: FSMContext) -> None:
        await message.answer('Enter password length:')
        await state.set_state(LengthStates.waiting_length)

    async def Generate_Password(self, message: Message, state: FSMContext) -> None:
        try:
            if message.text is None:
                raise ValueError('message is empty')

            length: int = NumberConverter.From_Str_To_Positive_Int(
                message.text)

            password: str = Generator.Generate_Password(length)

            await message.answer(f'Your password: {password}')
            await state.clear()
        except ValueError as e:
            await message.answer(f'Invalid input, error: {e}')

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

            user_ID: int = await self.repo.Find_User_By_Username(message.from_user.username)
            await self.repo.Associate_Password(user_ID, password, association)

            await message.answer(f'Successfully associated your password with {association}')
            await state.clear()

        except ValueError as e:
            await message.answer(f'Invalid input, error: {e}')

        except Exception as e:
            await message.answer(f'You already have this association')

    async def Print_User_Associations(self, message: Message, state: FSMContext) -> None:
        await state.clear()

        if message.from_user is None or message.from_user.username is None:
            await message.answer('Cant find your username')
            return

        try:
            user_id: int = await self.repo.Find_User_By_Username(message.from_user.username)
            associations: list[tuple[str, str]] = await self.repo.Find_Password_Associations(user_id)

            answer: str = Respondent.Create_Associations_List(associations)

            await message.answer(answer)
        except:
            await message.answer('You dont have any associations')

    async def Start_Association_Changing(self, message: Message, state: FSMContext) -> None:
        await message.answer('Enter a theme to associate and new password for it')
        await state.set_state(AssociationStates.waiting_changing_association)

    async def Change_Association(self, message: Message, state: FSMContext) -> None:
        if message.from_user is None or message.from_user.username is None:
            await message.answer('Cant find your name')
            return

        try:
            if message.text is None:
                raise ValueError('message is empty')

            user_id: int = await self.repo.Find_User_By_Username(message.from_user.username)

            association, password = MessageParser.ParseMessage(message.text)

            await self.repo.Change_Association_Password(user_id, password, association)

            await message.answer(f'Successfully changed your association {association}')
            await state.clear()

        except ValueError as e:
            await message.answer(f'Invalid input, error: {e}')

        except Exception as e:
            await message.answer(f'Error: {e}')
