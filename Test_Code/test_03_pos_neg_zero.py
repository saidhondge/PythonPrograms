import os
import sys
from importlib import import_module

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

check_number = import_module(
    "Code.03_pos_neg_zero"
).check_number


def test_positive():
    assert check_number(10) == "Positive"


def test_negative():
    assert check_number(-5) == "Negative"


def test_zero():
    assert check_number(0) == "Zero"


def test_large_positive():
    assert check_number(100) == "Positive"


def test_large_negative():
    assert check_number(-100) == "Negative"


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()

    print("All test cases passed.")