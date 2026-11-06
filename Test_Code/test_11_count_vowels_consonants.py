import os
import sys
from importlib import import_module

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

count_vowels_consonants = import_module(
    "Code.11_count_vowels_consonants"
).count_vowels_consonants


def test_hello_world():
    assert count_vowels_consonants("Hello World") == (3, 7)


def test_only_vowels():
    assert count_vowels_consonants("aeiou") == (5, 0)


def test_only_consonants():
    assert count_vowels_consonants("bcdf") == (0, 4)


def test_empty_string():
    assert count_vowels_consonants("") == (0, 0)


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()

    print("All test cases passed.")