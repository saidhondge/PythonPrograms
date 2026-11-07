import os
import sys
from importlib import import_module

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

character_frequency = import_module(
    "Code.14_character_frequency"
).character_frequency


def test_hello():
    assert character_frequency("hello") == {
        "h": 1, "e": 1, "l": 2, "o": 1
    }


def test_repeated_characters():
    assert character_frequency("aabb") == {
        "a": 2, "b": 2
    }


def test_empty_string():
    assert character_frequency("") == {}


def test_single_character():
    assert character_frequency("a") == {"a": 1}


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()

    print("All test cases passed.")