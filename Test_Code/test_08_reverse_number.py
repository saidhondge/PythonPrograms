import os
import sys
from importlib import import_module

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

reverse_number = import_module(
    "Code.08_reverse_number"
).reverse_number


def test_positive_number():
    assert reverse_number(1234) == 4321


def test_negative_number():
    assert reverse_number(-560) == -65


def test_zero():
    assert reverse_number(0) == 0


def test_trailing_zero():
    assert reverse_number(1200) == 21


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()

    print("All test cases passed.")