import pytest
from input_validation import get_integer_input, get_string_input

def test_get_integer_input(monkeypatch):
    """
    Test get_integer_input function with a list of numbers.
    """
    # List of numbers to test as input
    numbers = [100, 12000, 65, 350]
    
    # use the generator function to return each number in turn
    number_generator = (str(number) for number in numbers)
    
    # set the input attribute to the number from the number_generator using monkeypatch
    monkeypatch.setattr('builtins.input', lambda _: next(number_generator))
    
    # loop through the numbers list
    for expected_number in numbers:
        
        # check the expected outcome
        assert get_integer_input("Enter a number: ") == expected_number
        
def test_get_string_input(monkeypatch):
    """
    Test get_string_input function with a word
    """
    
    monkeypatch.setattr('builtins.input', lambda _: "hello")
    
    assert get_string_input("Enter a word: ") == "Hello" 