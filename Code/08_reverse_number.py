def reverse_number(num):
    sign = -1 if num < 0 else 1
    reversed_num = int(str(abs(num))[::-1])
    return sign * reversed_num


if __name__ == "__main__":
    print(reverse_number(1234))
    print(reverse_number(-560))