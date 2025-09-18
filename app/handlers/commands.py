from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.password.generator import Generator
from app.state.state import LengthStates, MatchStates
from app.repo.repo import Repo
from app.config import Config


class BotCommands:
    def __init__(self, repo: Repo) -> None:
        self.repo: Repo = repo

    @classmethod
    async def New(cls, cfg: Config) -> 'BotCommands':
        repo: Repo = await Repo.New(cfg)

        return cls(repo)

    async def Start_Handler(self, message: Message) -> None:
        if message.from_user is None:
            await message.answer(f'Hello, this is Password Generator Bot')
        else:
            await message.answer(f'Hello {message.from_user.first_name}, this is Password Generator Bot')

    async def Help_Handler(self, message: Message) -> None:
        answer: str = '''
    Commands:
    /start - start bot
    /help - display the list of available commands
    /generate - start generating a new password
    '''

        await message.answer(answer)

    async def Generate_Handler(self, message: Message, state: FSMContext) -> None:
        await message.answer('Enter password length:')
        await state.set_state(LengthStates.waiting_length)

    async def Input_Length(self, message: Message, state: FSMContext) -> None:
        try:
            if message.text is None:
                raise ValueError('message is empty')

            length: int = int(message.text)

            if length <= 0:
                raise ValueError('given not positive number')
            password: str = Generator.Generate_Password(length)

            await message.answer(f'Your password: {password}')
            await state.clear()
        except ValueError as e:
            await message.answer(f'Invalid input, error: {e}')

    async def Associate_Password(self, message: Message, state: FSMContext) -> None:
        await message.answer('Enter a theme to associate a password with it, for example: github')
        await state.set_state(MatchStates.waiting_match)

    async def Input_Password_Association(self, message: Message, state: FSMContext) -> None:
        # TODO: Write func
        pass
