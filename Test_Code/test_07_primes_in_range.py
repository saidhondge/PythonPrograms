import os
import sys
from importlib import import_module

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

primes_in_range = import_module(
    "Code.07_primes_in_range"
).primes_in_range


def test_range_1_to_20():
    assert primes_in_range(1, 20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_range_1_to_10():
    assert primes_in_range(1, 10) == [2, 3, 5, 7]


def test_range_10_to_20():
    assert primes_in_range(10, 20) == [11, 13, 17, 19]


def test_no_prime():
    assert primes_in_range(8, 10) == []


def test_single_prime():
    assert primes_in_range(7, 7) == [7]


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()

    print("All test cases passed.")