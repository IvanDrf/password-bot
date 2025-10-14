import pytest

from utils.converter import NumberConverter
from tests.converter.fixture import Correct_Numbers, Incorrect_Numbers


def test_NumberConverter(Correct_Numbers: list[str], Incorrect_Numbers: list[str]) -> None:
    for correct in Correct_Numbers:
        assert NumberConverter.From_Str_To_Positive_Int(
            correct) == int(correct)

    for incorrect in Incorrect_Numbers:
        with pytest.raises(ValueError) as error:
            NumberConverter.From_Str_To_Positive_Int(incorrect)
        assert 'given not a number' == str(
            error.value) or 'given not positive number' == str(error.value)
