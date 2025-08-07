import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("4 апреля 2023", "4 апреля 2023")
    ])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("Skypro", "Skypro"),
    ("", ""),
    ("   ", "   "),
    ])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected
