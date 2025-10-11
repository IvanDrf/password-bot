from aiogram.filters import CommandStart, Command
from aiogram import F
from typing import TYPE_CHECKING

from app.state.state import LengthStates, AssociationStates


class Registrator:
    if TYPE_CHECKING:
        from app.handlers.handler import Handler

    def __init__(self, handler: 'Handler') -> None:
        self.handler = handler

    def Register_Handlers(self) -> None:
        self.__Register_Start()
        self.__Register_Help()

        self.__Register_Password_Generation()
        self.__Register_Password_Association()
        self.__Register_Association_Print()
        self.__Register_Association_Changing()
        self.__Register_Association_Deletion()
        self.__Register_All_Associations_Deletion()

        self.__Register_Messages()

    def __Register_Start(self) -> None:
        self.handler.dp.message.register(self.handler.Start, CommandStart())

    def __Register_Help(self) -> None:
        self.handler.dp.message.register(self.handler.Help, Command('help'))

    def __Register_Password_Generation(self) -> None:
        self.handler.dp.message.register(
            self.handler.Start_Password_Generation, Command('generate'))
        self.handler.dp.message.register(
            self.handler.Generate_Password,  LengthStates.waiting_length)

    def __Register_Password_Association(self) -> None:
        self.handler.dp.message.register(
            self.handler.Start_Password_Association, Command('associate'))
        self.handler.dp.message.register(
            self.handler.Associate_Password, AssociationStates.waiting_new_association)

    def __Register_Association_Print(self) -> None:
        self.handler.dp.message.register(
            self.handler.Print_User_Associations, Command('my'))

    def __Register_Association_Changing(self) -> None:
        self.handler.dp.message.register(
            self.handler.Start_Association_Changing, Command('change'))
        self.handler.dp.message.register(
            self.handler.Change_Association, AssociationStates.waiting_changing_association)

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

    def __Register_Messages(self) -> None:
        self.handler.dp.message.register(self.handler.Message_Handler, F.text)
        self.handler.dp.message.register(
            self.handler.Message_Handler, F.sticker)
        self.handler.dp.message.register(self.handler.Message_Handler, F.voice)
        self.handler.dp.message.register(self.handler.Message_Handler, F.photo)
