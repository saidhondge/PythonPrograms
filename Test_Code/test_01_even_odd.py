import os
import sys
from importlib import import_module

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

even_odd = import_module("Code.01_even_odd").even_odd


def test_even():
    assert even_odd(10) == "Even"

def test_odd():
    assert even_odd(7) == "Odd"

def test_zero():
    assert even_odd(0) == "Even"

def test_negative_even():
    assert even_odd(-4) == "Even"

def test_negative_odd():
    assert even_odd(-5) == "Odd"


if __name__ == "__main__":
    for _name, _fn in list(globals().items()):
        if _name.startswith("test_") and callable(_fn):
            _fn()
    print("All test cases passed.")