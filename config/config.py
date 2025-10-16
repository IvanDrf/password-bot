from dotenv import load_dotenv
from os import getenv
from typing import cast, Final
import json

load_dotenv()


class Config:
    def __init__(self, token: str, db_name: str, up_migrations_path: str, down_migrations_path: str, key: str, logger_level: str) -> None:
        self.token: Final = token
        self.db_name: Final = db_name
        self.up_migrations_path: Final = up_migrations_path
        self.down_migrations_path: Final = down_migrations_path
        self.key: Final = key
        self.logger_level: Final = logger_level

    @classmethod
    def New(cls) -> 'Config':
        if getenv('TOKEN') is None:
            raise ValueError('cant get bot token in env from env')

        if getenv('DB_NAME') is None:
            raise ValueError('cant get database name from env')

        if getenv('UP_MIGRATIONS_PATH') is None:
            raise ValueError('cant get up migrations path from env')

        if getenv('DOWN_MIGRATIONS_PATH') is None:
            raise ValueError('cant get down migrations path from env')

        if getenv('KEY') is None:
            raise ValueError('cant get key for encryption from env')

        if getenv('LEVEL') is None:
            raise ValueError('cant get logger level from env')

        return Config(cast(str, getenv('TOKEN')), cast(str, getenv('DB_NAME')), cast(str, getenv('UP_MIGRATIONS_PATH')), cast(str, getenv('DOWN_MIGRATIONS_PATH')), cast(str, getenv('KEY')), cast(str, getenv('LEVEL')))
