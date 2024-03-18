def break_str(str):
    words = str.split(" ")
    return words


def sort_str(words):
    return sorted(words)


def print_str(str):
    words = break_str(str)
    sort_words = sort_str(words)
    print(str)
    print(sort_words)
    print(sort_words.pop(0))
    print(sort_words.pop(-1))


if __name__ == "__main__":
    str1 = input()
    print_str(str1)
