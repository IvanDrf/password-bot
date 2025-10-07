from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.commands.commands import BotCommands


class HelpHandler:
    def __init__(self, commands: BotCommands) -> None:
        self.commands: BotCommands = commands

    async def Help(self, message: Message, state: FSMContext) -> None:
        await self.commands.Help(message, state)
