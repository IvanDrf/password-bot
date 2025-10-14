from aiogram.filters import Command, CommandStart
from typing import TYPE_CHECKING


class DefaultRegistrator:
    if TYPE_CHECKING:
        from app.handlers.handler import Handler

    def __init__(self, handler: 'Handler') -> None:
        self.handler = handler

    def _Register_Default_Handlers(self) -> None:
        self.__Register_Start()
        self.__Register_Help()

    def __Register_Start(self) -> None:
        self.handler.dp.message.register(self.handler.Start, CommandStart())

    def __Register_Help(self) -> None:
        self.handler.dp.message.register(self.handler.Help, Command('help'))
