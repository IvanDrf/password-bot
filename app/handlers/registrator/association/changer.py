from aiogram.filters import Command
from typing import TYPE_CHECKING

from app.state.state import AssociationStates


class ChangerRegistrator:
    if TYPE_CHECKING:
        from app.handlers.handler import Handler

    def __init__(self, handler: 'Handler') -> None:
        self.handler = handler

    def _Register_Association_Changing(self) -> None:
        self.handler.dp.message.register(
            self.handler.Start_Association_Changing, Command('change'))
        self.handler.dp.message.register(
            self.handler.Change_Association, AssociationStates.waiting_changing_association)
