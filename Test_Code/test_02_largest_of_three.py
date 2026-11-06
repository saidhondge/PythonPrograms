import os
import sys
from importlib import import_module

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

largest_of_three = import_module(
    "Code.02_largest_of_three"
).largest_of_three


def test_first_largest():
    assert largest_of_three(10, 20, 15) == 20

def test_second_largest():
    assert largest_of_three(30, 10, 20) == 30

def test_third_largest():
    assert largest_of_three(10, 15, 25) == 25

def test_equal_numbers():
    assert largest_of_three(10, 10, 10) == 10

def test_negative_numbers():
    assert largest_of_three(-5, -2, -8) == -2


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()

    print("All test cases passed.")