def is_palindrome_number(num):
    if num < 0:
        return False

    return num == int(str(num)[::-1])


if __name__ == "__main__":
    print(is_palindrome_number(121))
    print(is_palindrome_number(123))