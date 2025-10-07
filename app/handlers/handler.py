from aiogram import Dispatcher

from config.config import Config
from app.commands.commands import BotCommands
from app.handlers.registrator.registrator import Registrator

from app.handlers.default.start import StartHandler
from app.handlers.default.help import HelpHandler
from app.handlers.password.password import PasswordHandler
from app.handlers.association.association import AssociationHandler
from app.handlers.message.message import MessageHandler


class Handler(StartHandler, HelpHandler, PasswordHandler, AssociationHandler, MessageHandler):
    dp: Dispatcher = Dispatcher()

    def __init__(self, commands: BotCommands) -> None:
        PasswordHandler.__init__(self, commands)
        AssociationHandler.__init__(self, commands)
        MessageHandler.__init__(self)

        self.commands: BotCommands = commands

    @classmethod
    async def New(cls, cfg: Config) -> 'Handler':
        cmds: BotCommands = await BotCommands.New(cfg)

        return cls(cmds)

    def Register_Handlers(self) -> None:
        Registrator(self).Register_Handlers()
