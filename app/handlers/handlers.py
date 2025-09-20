from aiogram import Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State

from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from app.state.state import LengthStates, AssociationStates

from app.config import Config
from app.handlers.commands import BotCommands
from app.handlers.messages import Message_Handler


class Handler:
    dp: Dispatcher = Dispatcher()

    def __init__(self, cmds: BotCommands) -> None:
        self.commands: BotCommands = cmds

    @classmethod
    async def New(cls, cfg: Config) -> 'Handler':
        cmds: BotCommands = await BotCommands.New(cfg)

        return cls(cmds)

    def Register_Handlers(self) -> None:
        self.__Register_Start()
        self.__Register_Help()

        self.__Register_Password_Generation()
        self.__Register_Password_Association()
        self.__Register_Association_Print()
        self.__Register_Association_Changing()

        self.__Register_Messages()

    async def Start_Handler(self, message: Message, state: FSMContext) -> None:
        await self.commands.Start_Handler(message, state)

    async def Help_Handler(self, message: Message, state: FSMContext) -> None:
        await self.commands.Help_Handler(message, state)

    async def Start_Password_Generation(self, message: Message, state: FSMContext) -> None:
        await self.commands.Start_Password_Generation(message, state)

    async def Generate_Password(self, message: Message, state: FSMContext) -> None:
        await self.commands.Generate_Password(message, state)

    async def Start_Password_Association(self, message: Message, state: FSMContext) -> None:
        await self.commands.Start_Password_Association(message, state)

    async def Associate_Password(self, message: Message, state: FSMContext) -> None:
        await self.commands.Associate_Password(message, state)

    async def Print_User_Associations(self, message: Message, state: FSMContext) -> None:
        await self.commands.Print_User_Associations(message, state)

    async def Start_Association_Changing(self, message: Message, state: FSMContext) -> None:
        await self.commands.Start_Association_Changing(message, state)

    async def Change_Association(self, message: Message, state: FSMContext) -> None:
        await self.commands.Change_Association(message, state)

    async def Message_Handler(self, message: Message, state: FSMContext) -> None:
        await Message_Handler(message, state)

    def __Register_Start(self) -> None:
        self.dp.message.register(self.Start_Handler, CommandStart())

    def __Register_Help(self) -> None:
        self.dp.message.register(self.Help_Handler, Command('help'))

    def __Register_Password_Generation(self) -> None:
        self.dp.message.register(
            self.Start_Password_Generation, Command('generate'))
        self.dp.message.register(
            self.Generate_Password,  LengthStates.waiting_length)

    def __Register_Password_Association(self) -> None:
        self.dp.message.register(
            self.Start_Password_Association, Command('associate'))
        self.dp.message.register(
            self.Associate_Password, AssociationStates.waiting_new_association)

    def __Register_Association_Print(self) -> None:
        self.dp.message.register(self.Print_User_Associations, Command('my'))

    def __Register_Association_Changing(self) -> None:
        self.dp.message.register(
            self.Start_Association_Changing, Command('change'))
        self.dp.message.register(
            self.Change_Association, AssociationStates.waiting_changing_association)

    def __Register_Messages(self) -> None:
        self.dp.message.register(self.Message_Handler, F.text)
