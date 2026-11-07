import os
import sys
from importlib import import_module

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

find_duplicates = import_module(
    "Code.19_find_duplicates"
).find_duplicates


def test_normal_list():
    assert find_duplicates([1, 2, 3, 2, 4, 3]) == [2, 3]


def test_no_duplicates():
    assert find_duplicates([1, 2, 3, 4]) == []


def test_all_duplicates():
    assert find_duplicates([5, 5, 5]) == [5]


def test_empty_list():
    assert find_duplicates([]) == []


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()

    print("All test cases passed.")