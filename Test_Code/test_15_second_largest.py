import os
import sys
from importlib import import_module

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

second_largest = import_module(
    "Code.15_second_largest"
).second_largest


def test_normal_list():
    assert second_largest([10, 20, 30, 40, 50]) == 40


def test_with_duplicates():
    assert second_largest([10, 20, 20, 30]) == 20


def test_negative_numbers():
    assert second_largest([-10, -20, -30]) == -20


def test_same_numbers():
    assert second_largest([5, 5, 5]) == None


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()

    print("All test cases passed.")