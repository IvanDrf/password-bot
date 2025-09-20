from dotenv import load_dotenv
from os import getenv
from typing import cast

load_dotenv()


class Config:
    def __init__(self) -> None:
        if getenv('TOKEN') is None:
            raise ValueError('cant get bot token in env')

        if getenv('DB_NAME') is None:
            raise ValueError('cant get database name')

        self.token: str = cast(str, getenv('TOKEN'))
        self.db_name: str = cast(str, getenv('DB_NAME'))
