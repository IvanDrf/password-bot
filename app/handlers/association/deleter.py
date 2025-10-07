from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.commands.commands import BotCommands


class DeleteHandler:
    def __init__(self, commands: BotCommands) -> None:
        self.commands: BotCommands = commands

    async def Start_Association_Deletion(self, message: Message, state: FSMContext) -> None:
        await self.commands.Start_Association_Deletion(message, state)

    async def Delete_Association(self, message: Message, state: FSMContext) -> None:
        await self.commands.Delete_Association(message, state)

    async def Start_All_Associations_Deletion(self, message: Message, state: FSMContext) -> None:
        await self.commands.Start_All_Associations_Deletion(message, state)

    async def Delete_All_Associations(self, message: Message, state: FSMContext) -> None:
        await self.commands.Delete_All_Associations(message, state)
