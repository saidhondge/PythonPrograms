import os
import sys
from importlib import import_module

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

factorial = import_module(
    "Code.04_factorial"
).factorial


def test_factorial_five():
    assert factorial(5) == 120


def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_one():
    assert factorial(1) == 1


def test_factorial_three():
    assert factorial(3) == 6


def test_negative_number():
    assert factorial(-5) == "Not Defined"


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()

    print("All test cases passed.")