from aiogram.filters import Command
from typing import TYPE_CHECKING

from app.state.state import LengthStates


class PasswordRegistrator:
    if TYPE_CHECKING:
        from app.handlers.handler import Handler

    def __init__(self, handler: 'Handler') -> None:
        self.handler = handler

    def _Register_Password_Generation(self) -> None:
        self.handler.dp.message.register(
            self.handler.Start_Password_Generation, Command('generate'))
        self.handler.dp.message.register(
            self.handler.Generate_Password,  LengthStates.waiting_length)
