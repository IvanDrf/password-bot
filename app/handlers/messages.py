from aiogram import F
from aiogram.types import Message

from .handlers import Handler


@Handler.dp.message(F.text)
async def Message_Handler(message: Message) -> None:
    if message.from_user is None:
        await message.answer('Sorry, but I dont get it, write /help to see available commands')
    else:
        await message.answer(f'Sorry {message.from_user.first_name}, but I dont get it, write /help to see available commands')
