from aiogram import F
from typing import TYPE_CHECKING


class MessageRegistrator:
    if TYPE_CHECKING:
        from app.handlers.handler import Handler

    def __init__(self, handler: 'Handler') -> None:
        self.handler = handler

    def _Register_Messages(self) -> None:
        self.handler.dp.message.register(self.handler.Message_Handler, F.text)
        self.handler.dp.message.register(
            self.handler.Message_Handler, F.sticker)
        self.handler.dp.message.register(self.handler.Message_Handler, F.voice)
        self.handler.dp.message.register(self.handler.Message_Handler, F.photo)
