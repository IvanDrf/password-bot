import pytest


@pytest.fixture
def Correct_Numbers() -> list[str]:
    return ['2', '13', '1', '35', '2', '1']


@pytest.fixture
def Incorrect_Numbers() -> list[str]:
    return ['w', '-5', 'q', 'wd', 'printf a']
