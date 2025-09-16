from aiogram import Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from .handlers import Handler


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
