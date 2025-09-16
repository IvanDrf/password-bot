from dotenv import load_dotenv
from os import getenv
from typing import cast

load_dotenv()


class Config:
    def __init__(self) -> None:
        if getenv('TOKEN') is None:
            raise ValueError('cant get bot token in env')

        self.token: str = cast(str, getenv('TOKEN'))
