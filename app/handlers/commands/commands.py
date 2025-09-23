from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.handlers.commands.associations import AssociationAdder, AssociationChanger, AssociationDeleter, AssociationPrinter
from app.handlers.commands.password import PasswordCreator
from app.handlers.commands.starter import Starter
from app.handlers.commands.helper import Helper
from app.repo.repo import Repo
from app.utils.encrypter import Encrypter
from config.config import Config


class BotCommands:
    def __init__(self, cfg: Config, repo: Repo) -> None:
        self.repo: Repo = repo

        self.starter: Starter = Starter(repo)
        self.helper: Helper = Helper()

        encrypter: Encrypter = Encrypter.New(cfg)

        self.password_creator: PasswordCreator = PasswordCreator(repo)
        self.association_adder: AssociationAdder = AssociationAdder(
            repo, encrypter)
        self.association_changer: AssociationChanger = AssociationChanger(
            repo, encrypter)
        self.association_deleter: AssociationDeleter = AssociationDeleter(repo)
        self.association_printer: AssociationPrinter = AssociationPrinter(
            repo, encrypter)

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
        await self.association_adder.Start_Password_Association(message, state)

    async def Associate_Password(self, message: Message, state: FSMContext) -> None:
        await self.association_adder.Associate_Password(message, state)

    async def Print_User_Associations(self, message: Message, state: FSMContext) -> None:
        await self.association_printer.Print_User_Associations(message, state)

    async def Start_Association_Changing(self, message: Message, state: FSMContext) -> None:
        await self.association_changer.Start_Association_Changing(message, state)

    async def Change_Association(self, message: Message, state: FSMContext) -> None:
        await self.association_changer.Change_Association(message, state)

    async def Start_Association_Deletion(self, message: Message, state: FSMContext) -> None:
        await self.association_deleter.Start_Association_Deletion(message, state)

    async def Delete_Association(self, message: Message, state: FSMContext) -> None:
        await self.association_deleter.Delete_Association(message, state)
