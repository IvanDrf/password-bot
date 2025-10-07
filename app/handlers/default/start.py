from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.commands.commands import BotCommands

class StartHandler:
    def __init__(self, commands: BotCommands) -> None:
        self.commands: BotCommands = commands

    async def Start(self, message: Message, state: FSMContext) -> None:
        await self.commands.Start(message, state)
