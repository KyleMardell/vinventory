import pytest
from input_validation import get_integer_input, get_integer_input_mock
from input_validation import get_string_input, get_list_input


def test_get_integer_input(monkeypatch):
    """
    Test get_integer_input function with a list of numbers.
    """
    # List of numbers to test as input
    numbers = [100, 12000, 65, 350]

    # use the generator function to return each number in turn
    number_generator = (str(number) for number in numbers)

    # set the input attribute to the number
    # from the number_generator using monkeypatch
    monkeypatch.setattr('builtins.input', lambda _: next(number_generator))

    # loop through the numbers list
    for expected_number in numbers:
        # check the expected outcome
        assert get_integer_input("message") == expected_number


def test_get_string_input(monkeypatch):
    """
    Test get_string_input function with a word
    """
    # set the input attribute to 'hello'
    monkeypatch.setattr('builtins.input', lambda _: "hello")
    # check the expected outcome (capitalized)
    assert get_string_input("message") == "Hello"


def test_get_list_input(monkeypatch):
    """
    Test the get_list_input function with a list of words
    """
    # set the input attribute to 'hello, world'
    monkeypatch.setattr('builtins.input', lambda _: "hello, world")
    # check the expected outcome
    assert get_list_input("message") == ["hello", "world"]

# Mock function tests


def test_get_integer_input_mock_valid(monkeypatch):
    """
    Test get_integer_input_mock for valid input
    """
    # set input to "10"
    monkeypatch.setattr('builtins.input', lambda _: "10")
    # check expected outcome
    assert get_integer_input_mock("Message") == 10


def test_get_integer_input_mock_invalid(monkeypatch):
    """
    Test get_integer_input_mock for invalid input
    """
    # set input to "hello"
    monkeypatch.setattr('builtins.input', lambda _: "hello")
    # check expected outcome
    message = "Error: Not a valid number."
    assert get_integer_input_mock("Message") == message


def test_get_integer_input_mock_negative(monkeypatch):
    """
    Test get_integer_input_mock for negative number input
    """
    # set input to "-5"
    monkeypatch.setattr('builtins.input', lambda _: "-5")
    # check expected outcome
    message = "Error: Must be a positive number."
    assert get_integer_input_mock("message") == message
