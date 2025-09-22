import pytest


@pytest.fixture
def associations() -> list[tuple[str, str]]:
    return [('first', 'second'), ('third', 'fourth'), ('fifth', 'sixth')]
