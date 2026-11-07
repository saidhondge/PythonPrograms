def word_frequency(text):
    frequency = {}

    words = text.lower().split()

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


if __name__ == "__main__":
    print(word_frequency("python is easy python is powerful"))