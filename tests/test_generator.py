from app.password.generator import Generator
from pytest import fixture


@fixture
def Length_List() -> list[int]:
    return [0, 5, 6, 10]


def test_Generator(Length_List) -> None:
    passwords: list[str] = []

    for length in Length_List:
        passwords.append(Generator.Generate_Password(length))

    for length, password in zip(Length_List, passwords):
        assert length == len(password)
