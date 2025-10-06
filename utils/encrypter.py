from typing import Any
from cryptography.fernet import Fernet

from config.config import Config


class Encrypter(Fernet):
    def __init__(self, key: str, backend: Any = None) -> None:
        if key[-1] != '=':
            key += '='
        super().__init__(key, backend)

    @classmethod
    def New(cls, cfg: Config) -> 'Encrypter':
        return cls(cfg.key + '=')
