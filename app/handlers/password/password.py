from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.commands.commands import BotCommands


class PasswordHandler:
    def __init__(self, commands: BotCommands) -> None:
        self.commands: BotCommands = commands

    async def Start_Password_Generation(self, message: Message, state: FSMContext) -> None:
        await self.commands.Start_Password_Generation(message, state)

    async def Generate_Password(self, message: Message, state: FSMContext) -> None:
        await self.commands.Generate_Password(message, state)
