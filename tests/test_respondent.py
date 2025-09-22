import pytest
from app.utils.respondent import Respondent


@pytest.fixture
def associations() -> list[tuple[str, str]]:
    return [('first', 'second'), ('third', 'fourth'), ('fifth', 'sixth')]


def test_Responder(associations: list[tuple[str, str]]) -> None:
    excepted: str = '1) first | second\n2) third | fourth\n3) fifth | sixth'

    assert excepted == Respondent.Create_Associations_List(associations)
