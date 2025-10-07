from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.commands.commands import BotCommands


class AddHandler:
    def __init__(self, commands: BotCommands) -> None:
        self.commands: BotCommands = commands

    async def Start_Password_Association(self, message: Message, state: FSMContext) -> None:
        await self.commands.Start_Password_Association(message, state)

    async def Associate_Password(self, message: Message, state: FSMContext) -> None:
        await self.commands.Associate_Password(message, state)
