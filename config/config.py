from dotenv import load_dotenv
from os import getenv
from typing import cast

load_dotenv()


class Config:
    def __init__(self, token: str, db_name: str) -> None:
        self.token: str = token
        self.db_name: str = db_name

    @classmethod
    def New(cls) -> 'Config':
        if getenv('TOKEN') is None:
            raise ValueError('cant get bot token in env')

        if getenv('DB_NAME') is None:
            raise ValueError('cant get database name')

        return Config(cast(str, getenv('TOKEN')), cast(str, getenv('DB_NAME')))
