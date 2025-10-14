import pytest


@pytest.fixture
def Correct_Messages() -> list[str]:
    return ['a b', 'first second', 'hello world']


@pytest.fixture
def Incorrect_Messages() -> list[str]:
    return ['a', '', 'first_second']
