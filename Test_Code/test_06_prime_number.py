import os
import sys
from importlib import import_module

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

is_prime = import_module(
    "Code.06_prime_number"
).is_prime


def test_prime_number():
    assert is_prime(7) == True


def test_non_prime_number():
    assert is_prime(10) == False


def test_two():
    assert is_prime(2) == True


def test_zero():
    assert is_prime(0) == False


def test_negative_number():
    assert is_prime(-5) == False


def test_one():
    assert is_prime(1) == False


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()

    print("All test cases passed.")