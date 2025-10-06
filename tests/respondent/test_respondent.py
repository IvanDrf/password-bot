import pytest
from utils.respondent import Respondent
from tests.respondent.fixture import associations


def test_Responder(associations: list[list[str]]) -> None:
    excepted: str = '1) first | second\n2) third | fourth\n3) fifth | sixth'

    assert excepted == Respondent.Create_Associations_List(associations)
