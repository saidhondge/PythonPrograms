import os
import sys
from importlib import import_module

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

remove_duplicates = import_module(
    "Code.16_remove_duplicates"
).remove_duplicates


def test_normal_list():
    assert remove_duplicates([1, 2, 2, 3, 4]) == [1, 2, 3, 4]


def test_all_duplicates():
    assert remove_duplicates([5, 5, 5]) == [5]


def test_no_duplicates():
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]


def test_empty_list():
    assert remove_duplicates([]) == []


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()

    print("All test cases passed.")