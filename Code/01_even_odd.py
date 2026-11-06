def even_odd(num):
    """Return "Even" or "Odd" for an integer."""
    if num % 2 == 0:
        return "Even"
    return "Odd"


if __name__ == "__main__":
    print(even_odd(20))
    print(even_odd(11))