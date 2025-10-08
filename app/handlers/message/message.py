from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.message.message import Messager


class MessageHandler:
    async def Message_Handler(self, message: Message, state: FSMContext) -> None:
        await Messager.Answer(message, state)
