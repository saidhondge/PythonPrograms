def find_duplicates(numbers):
    duplicates = []
    seen = set()

    for num in numbers:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        else:
            seen.add(num)

    return duplicates


if __name__ == "__main__":
    print(find_duplicates([1, 2, 3, 2, 4, 3, 5]))