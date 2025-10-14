import pytest

from tests.parser.fixture import Correct_Messages, Incorrect_Messages
from utils.parser import MessageParser


def test_Correct_Message_MessageParser(Correct_Messages: list[str]) -> None:
    for correct_message in Correct_Messages:
        first, second = correct_message.split()

        association, password = MessageParser.ParseMessage(correct_message)

        assert first == association
        assert second == password


def test_Incorrect_Message_Parser(Incorrect_Messages: list[str]) -> None:
    for incorrect_message in Incorrect_Messages:
        with pytest.raises(ValueError) as error:
            MessageParser.ParseMessage(incorrect_message)

        assert 'format should be "first" "second"' == str(error.value)
