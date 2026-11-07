import os
import sys
from importlib import import_module

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

common_elements = import_module(
    "Code.17_common_elements"
).common_elements


def test_normal_lists():
    assert common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]


def test_no_common_elements():
    assert common_elements([1, 2], [3, 4]) == []


def test_duplicate_elements():
    assert common_elements([1, 1, 2, 3], [1, 2, 2]) == [1, 2]


def test_empty_lists():
    assert common_elements([], []) == []


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()

    print("All test cases passed.")