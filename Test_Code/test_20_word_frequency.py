import os
import sys
from importlib import import_module

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

word_frequency = import_module(
    "Code.20_word_frequency"
).word_frequency


def test_normal_sentence():
    assert word_frequency("python is easy python is powerful") == {
        "python": 2,
        "is": 2,
        "easy": 1,
        "powerful": 1
    }


def test_repeated_word():
    assert word_frequency("hello hello hello") == {
        "hello": 3
    }


def test_uppercase_words():
    assert word_frequency("Python PYTHON") == {
        "python": 2
    }


def test_empty_string():
    assert word_frequency("") == {}


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()

    print("All test cases passed.")