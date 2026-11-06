import os
import sys
from importlib import import_module

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

fibonacci_series = import_module(
    "Code.05_fibonacci_series"
).fibonacci_series


def test_seven_terms():
    assert fibonacci_series(7) == [0, 1, 1, 2, 3, 5, 8]


def test_one_term():
    assert fibonacci_series(1) == [0]


def test_two_terms():
    assert fibonacci_series(2) == [0, 1]


def test_zero_terms():
    assert fibonacci_series(0) == []


def test_negative_terms():
    assert fibonacci_series(-3) == []


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()

    print("All test cases passed.")
    