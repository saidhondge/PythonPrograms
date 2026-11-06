import os
import sys
from importlib import import_module

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

sum_of_digits = import_module(
    "Code.10_sum_of_digits"
).sum_of_digits


def test_normal_number():
    assert sum_of_digits(1234) == 10


def test_single_digit():
    assert sum_of_digits(5) == 5


def test_zero():
    assert sum_of_digits(0) == 0


def test_negative_number():
    assert sum_of_digits(-123) == 6


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()

    print("All test cases passed.")