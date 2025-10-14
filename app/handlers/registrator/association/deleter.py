from aiogram.filters import Command
from typing import TYPE_CHECKING

from app.state.state import AssociationStates


class DeleterRegistrator:
    if TYPE_CHECKING:
        from app.handlers.handler import Handler

    def __init__(self, handler: 'Handler') -> None:
        self.handler = handler

    def _Register_Deletion(self) -> None:
        self.__Register_Association_Deletion()
        self.__Register_All_Associations_Deletion()

    def __Register_Association_Deletion(self) -> None:
        self.handler.dp.message.register(
            self.handler.Start_Association_Deletion, Command('del'))
        self.handler.dp.message.register(
            self.handler.Delete_Association, AssociationStates.waiting_deletion_association)

    def __Register_All_Associations_Deletion(self) -> None:
        self.handler.dp.message.register(
            self.handler.Start_All_Associations_Deletion, Command('del_all'))
        self.handler.dp.message.register(
            self.handler.Delete_All_Associations, AssociationStates.waiting_deletion_all_associations)
