from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.commands.commands import BotCommands


class ChangeHandler:
    def __init__(self, commands: BotCommands) -> None:
        self.commands: BotCommands = commands

    async def Start_Association_Changing(self, message: Message, state: FSMContext) -> None:
        await self.commands.Start_Association_Changing(message, state)

    async def Change_Association(self, message: Message, state: FSMContext) -> None:
        await self.commands.Change_Association(message, state)
