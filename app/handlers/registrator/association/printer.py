from aiogram.filters import Command
from typing import TYPE_CHECKING


class PrinterRegistrator:
    if TYPE_CHECKING:
        from app.handlers.handler import Handler

    def __init__(self, handler: 'Handler') -> None:
        self.handler = handler

    def _Register_Association_Print(self) -> None:
        self.handler.dp.message.register(
            self.handler.Print_User_Associations, Command('my'))
