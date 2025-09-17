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
        self.dp.message.register(
            self.Generate_Handler, Command('generate'))
        self.dp.message.register(
            self.Input_Length,  LengthStates.waiting_length)

        self.dp.message.register(self.Message_Handler, F.text)

    # @dp.message(CommandStart())
    async def Start_Handler(self, message: Message) -> None:
        await self.commands.Start_Handler(message)

    # @dp.message(Command('help'))
    async def Help_Handler(self, message: Message) -> None:
        await self.commands.Help_Handler(message)

    # @dp.message(Command('generate'))
    async def Generate_Handler(self, message: Message, state: FSMContext) -> None:
        await self.commands.Generate_Handler(message, state)

    # @dp.message(LengthStates.waiting_length)
    async def Input_Length(self, message: Message, state: FSMContext) -> None:
        await self.commands.Input_Length(message, state)

    # @dp.message(Command('match'))
    async def Associate_Password(self, message: Message, state: FSMContext) -> None:
        await self.commands.Associate_Password(message, state)

    # @dp.message(MatchStates.waiting_match)
    async def Input_Password_Association(self, message: Message, state: FSMContext) -> None:
        pass

    # @dp.message(F.text)
    async def Message_Handler(self, message: Message) -> None:
        await Message_Handler(message)
