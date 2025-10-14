from aiogram.filters import Command
from typing import TYPE_CHECKING

from app.state.state import AssociationStates


class AdderRegistrator:
    if TYPE_CHECKING:
        from app.handlers.handler import Handler

    def __init__(self, handler: 'Handler') -> None:
        self.handler = handler

    def _Register_Password_Association(self) -> None:
        self.handler.dp.message.register(
            self.handler.Start_Password_Association, Command('associate'))
        self.handler.dp.message.register(
            self.handler.Associate_Password, AssociationStates.waiting_new_association)
