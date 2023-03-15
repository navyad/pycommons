import pytest

from src.validators import (
    validate_mobile_number,
    validate_gstin)


@pytest.mark.parametrize(
    "test_input, expected",
    [("9847567388", True),
     ("+917983746573", True),
     ("+916839273644", False)])
def test_mobile_number(test_input, expected):
    assert validate_mobile_number(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [("07ABCDE1234F1Z5", True),
     ("08FGHIJ2345K2Z6", True),
     ("07AB1234CDE1FZ5", False),
     ("07ABCD1234F1Z", False)])
def test_gstin(test_input, expected):
    assert validate_gstin(test_input) == expected
