import os
import sys
from importlib import import_module

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

is_palindrome_string = import_module(
    "Code.13_palindrome_string"
).is_palindrome_string


def test_palindrome():
    assert is_palindrome_string("madam") == True


def test_not_palindrome():
    assert is_palindrome_string("hello") == False


def test_uppercase():
    assert is_palindrome_string("MADAM") == True


def test_spaces():
    assert is_palindrome_string("nurses run") == True


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()

    print("All test cases passed.")