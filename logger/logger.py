import logging
from typing import Final, Literal
from sys import stdout

from config.config import Config


def Setup_Logger(cfg: Config) -> None:
    level: Literal[10, 30, 40, 20] = __Set_Logger_Level(cfg)
    logging.basicConfig(
        level=level,
        stream=stdout
    )


class Level:
    debug: Final = 'debug'
    warn: Final = 'warn'
    error: Final = 'error'
    info: Final = 'info'


def __Set_Logger_Level(cfg: Config) -> Literal[10, 30, 40, 20]:
    match cfg.logger_level:
        case Level.debug:
            return logging.DEBUG

        case Level.warn:
            return logging.WARN

        case Level.error:
            return logging.ERROR

        case Level.info:
            return logging.INFO

        case _:
            raise ValueError('invalid logger level in env')
