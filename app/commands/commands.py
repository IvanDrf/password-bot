from app.commands.association.association import Associationer

from app.commands.password.password import PasswordCreator
from app.commands.default.starter import Starter
from app.commands.default.helper import Helper
from app.repo.repo import Repo
from utils.encrypter import Encrypter
from config.config import Config


class BotCommands(Starter, Helper, PasswordCreator, Associationer):
    def __init__(self, cfg: Config, repo: Repo) -> None:
        self.repo: Repo = repo

        Starter.__init__(self, repo)
        Helper.__init__(self)

        encrypter: Encrypter = Encrypter.New(cfg)

        PasswordCreator.__init__(self, repo)
        Associationer.__init__(self, repo, encrypter)

    @classmethod
    async def New(cls, cfg: Config) -> 'BotCommands':
        repo: Repo = await Repo.New(cfg)

        return cls(cfg, repo)
