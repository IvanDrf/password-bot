from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.messages.messages import Message_Handler


class MessageHandler:
    async def Message_Handler(self, message: Message, state: FSMContext) -> None:
        await Message_Handler(message, state)
