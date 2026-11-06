def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


if __name__ == "__main__":
    print(largest_of_three(10, 20, 15))