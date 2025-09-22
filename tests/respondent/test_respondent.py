import pytest
from app.utils.respondent import Respondent
from tests.respondent.fixture import *


def test_Responder(associations: list[tuple[str, str]]) -> None:
    excepted: str = '1) first | second\n2) third | fourth\n3) fifth | sixth'

    assert excepted == Respondent.Create_Associations_List(associations)
