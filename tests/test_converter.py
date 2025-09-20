from app.utils.converter import NumberConverter, MessageParser
import pytest


@pytest.fixture
def Correct_Numbers() -> list[str]:
    return ['2', '13', '1', '35', '2', '1']


@pytest.fixture
def Incorrect_Numbers() -> list[str]:
    return ['w', '-5', 'q', 'wd', 'printf a']


def test_NumberConverter(Correct_Numbers, Incorrect_Numbers) -> None:
    for correct in Correct_Numbers:
        assert NumberConverter.From_Str_To_Positive_Int(
            correct) == int(correct)

    for incorrect in Incorrect_Numbers:
        with pytest.raises(ValueError) as error:
            NumberConverter.From_Str_To_Positive_Int(incorrect)
        assert 'given not a number' == str(
            error.value) or 'given not positive number' == str(error.value)


@pytest.fixture
def Correct_Messages() -> list[str]:
    return ['a b', 'first second', 'hello world']


@pytest.fixture
def Incorrect_Messages() -> list[str]:
    return ['a', '', 'first_second']


def test_MessageParser(Correct_Messages, Incorrect_Messages) -> None:
    for correct_message in Correct_Messages:
        first, second = correct_message.split()

        association, password = MessageParser.ParseMessage(correct_message)

        assert first == association
        assert second == password

    for incorrect_message in Incorrect_Messages:
        with pytest.raises(ValueError) as error:
            MessageParser.ParseMessage(incorrect_message)

        assert 'format should be name password' == str(error.value)
