import os
import sys
from importlib import import_module

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

find_missing_number = import_module(
    "Code.18_missing_number"
).find_missing_number


def test_normal_list():
    assert find_missing_number([1, 2, 4, 5]) == 3


def test_missing_first_number():
    assert find_missing_number([2, 3, 4, 5]) == 1


def test_missing_last_number():
    assert find_missing_number([1, 2, 3, 4]) == 5


def test_two_numbers():
    assert find_missing_number([1]) == 2


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()

    print("All test cases passed.")