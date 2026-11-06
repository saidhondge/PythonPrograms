import os
import sys
from importlib import import_module

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

is_palindrome_number = import_module(
    "Code.09_palindrome_number"
).is_palindrome_number


def test_palindrome():
    assert is_palindrome_number(121) == True


def test_not_palindrome():
    assert is_palindrome_number(123) == False


def test_single_digit():
    assert is_palindrome_number(7) == True


def test_negative_number():
    assert is_palindrome_number(-121) == False


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()

    print("All test cases passed.")