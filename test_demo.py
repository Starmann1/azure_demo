import pytest

def add_numbers(a, b):
    return a + b

def test_addition_success():
    assert add_numbers(2, 3) == 5

def test_addition_failure():
    # This is designed to pass, but you can change the 10 to see a failure
    assert add_numbers(5, 5) == 10
