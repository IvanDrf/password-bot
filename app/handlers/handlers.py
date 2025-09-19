from aiogram import Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State

from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from app.state.state import LengthStates, MatchStates

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
        self.dp.message.register(self.Start_Handler, CommandStart())
        self.dp.message.register(self.Help_Handler, Command('help'))

        self.dp.message.register(self.Generate_Handler, Command('generate'))
        self.dp.message.register(
            self.Input_Length,  LengthStates.waiting_length)

        self.dp.message.register(self.Associate_Password, Command('associate'))
        self.dp.message.register(
            self.Input_Password_Association, MatchStates.waiting_match)

        self.dp.message.register(self.Print_User_Associations, Command('my'))

        self.dp.message.register(self.Message_Handler, F.text)

    async def Start_Handler(self, message: Message) -> None:
        await self.commands.Start_Handler(message)

    async def Help_Handler(self, message: Message) -> None:
        await self.commands.Help_Handler(message)

    async def Generate_Handler(self, message: Message, state: FSMContext) -> None:
        await self.commands.Generate_Password(message, state)

    async def Input_Length(self, message: Message, state: FSMContext) -> None:
        await self.commands.Input_Password_Length(message, state)

    async def Associate_Password(self, message: Message, state: FSMContext) -> None:
        await self.commands.Associate_Password(message, state)

    async def Input_Password_Association(self, message: Message, state: FSMContext) -> None:
        await self.commands.Input_Password_Association(message, state)

    async def Print_User_Associations(self, message: Message) -> None:
        await self.commands.Print_User_Associations(message)

    async def Message_Handler(self, message: Message) -> None:
        await Message_Handler(message)
