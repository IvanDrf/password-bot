from string import digits, ascii_letters, punctuation
from typing import Final
from random import choice


class Generator():
    __characters: Final = digits + ascii_letters + punctuation

    @staticmethod
    def Generate_Password(length: int) -> str:
        return ''.join(choice(Generator.__characters) for _ in range(length))
