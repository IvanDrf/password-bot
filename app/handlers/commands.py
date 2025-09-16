from aiogram import Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from .handlers import Handler
from password.generator import Generator
from state.state import LengthStates


@Handler.dp.message(CommandStart())
async def Start_Handler(message: Message) -> None:
    if message.from_user is None:
        await message.answer(f'Hello, this is Password Generator Bot')
    else:
        await message.answer(f'Hello {message.from_user.first_name}, this is Password Generator Bot')


@Handler.dp.message(Command('help'))
async def Help_Handler(message: Message) -> None:
    answer: str = '''
Commands:
/start - start bot
/help - display the list of available commands
/generate - start generating a new password
'''

    await message.answer(answer)


@Handler.dp.message(Command('generate'))
async def Generate_Handler(message: Message, state: FSMContext) -> None:
    await message.answer('Enter password length:')
    await state.set_state(LengthStates.waiting_length)


@Handler.dp.message(LengthStates.waiting_length)
async def Input_Length(message: Message, state: FSMContext) -> None:
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
