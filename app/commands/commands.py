from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.commands.association.association import Associationer

from app.commands.password.password import PasswordCreator
from app.commands.default.starter import Starter
from app.commands.default.helper import Helper
from app.repo.repo import Repo
from utils.encrypter import Encrypter
from config.config import Config


class BotCommands:
    def __init__(self, cfg: Config, repo: Repo) -> None:
        self.repo: Repo = repo

        self.starter: Starter = Starter(repo)
        self.helper: Helper = Helper()

        encrypter: Encrypter = Encrypter.New(cfg)

        self.password_creator: PasswordCreator = PasswordCreator(repo)

        self.associationer: Associationer = Associationer(repo, encrypter)

    @classmethod
    async def New(cls, cfg: Config) -> 'BotCommands':
        repo: Repo = await Repo.New(cfg)

        return cls(cfg, repo)

    async def Start(self, message: Message, state: FSMContext) -> None:
        await self.starter.Start(message, state)

    async def Help(self, message: Message, state: FSMContext) -> None:
        await self.helper.Help(message, state)

    async def Start_Password_Generation(self, message: Message, state: FSMContext) -> None:
        await self.password_creator.Start_Password_Generation(message, state)

    async def Generate_Password(self, message: Message, state: FSMContext) -> None:
        await self.password_creator.Generate_Password(message, state)

    async def Start_Password_Association(self, message: Message, state: FSMContext) -> None:
        await self.associationer.Start_Password_Association(message, state)

    async def Associate_Password(self, message: Message, state: FSMContext) -> None:
        await self.associationer.Associate_Password(message, state)

    async def Print_User_Associations(self, message: Message, state: FSMContext) -> None:
        await self.associationer.Print_User_Associations(message, state)

    async def Start_Association_Changing(self, message: Message, state: FSMContext) -> None:
        await self.associationer.Start_Association_Changing(message, state)

    async def Change_Association(self, message: Message, state: FSMContext) -> None:
        await self.associationer.Change_Association(message, state)

    async def Start_Association_Deletion(self, message: Message, state: FSMContext) -> None:
        await self.associationer.Start_Association_Deletion(message, state)

    async def Delete_Association(self, message: Message, state: FSMContext) -> None:
        await self.associationer.Delete_Association(message, state)

    async def Start_All_Associations_Deletion(self, message: Message, state: FSMContext) -> None:
        await self.associationer.Start_All_Associations_Deletion(message, state)

    async def Delete_All_Associations(self, message: Message, state: FSMContext) -> None:
        await self.associationer.Delete_All_Associations(message, state)
