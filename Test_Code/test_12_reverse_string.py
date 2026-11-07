import os
import sys
from importlib import import_module

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

reverse_string = import_module(
    "Code.12_reverse_string"
).reverse_string


def test_normal_string():
    assert reverse_string("Python") == "nohtyP"


def test_hello():
    assert reverse_string("Hello") == "olleH"


def test_empty_string():
    assert reverse_string("") == ""


def test_single_character():
    assert reverse_string("A") == "A"


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()

    print("All test cases passed.")