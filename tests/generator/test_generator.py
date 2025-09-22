from app.password.generator import PasswordGenerator
from tests.generator.fixture import *


def test_Generator(Length_List) -> None:
    passwords: list[str] = []

    for length in Length_List:
        passwords.append(PasswordGenerator.Generate_Password(length))

    for length, password in zip(Length_List, passwords):
        assert length == len(password)
