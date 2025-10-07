from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.commands.commands import BotCommands


class PrintHandler:
    def __init__(self, commands: BotCommands) -> None:
        self.commands: BotCommands = commands

    async def Print_User_Associations(self, message: Message, state: FSMContext) -> None:
        await self.commands.Print_User_Associations(message, state)
