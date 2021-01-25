def is_unique_1(string):
    if len(string) > 128:
        return False
    chars = [False] * 128
    for char in string:
        val = ord(char)
        if chars[val]:
            print("False")
            return False
        else:
            chars[val] = True
    print("True")
    return True


def is_unique_2(string):
    print(len(set(string)) == len(string))
    return len(set(string)) == len(string)


# Test Cases
is_unique_1("abcdefg")
is_unique_2("abcdefg")
is_unique_1("add333")
is_unique_2("add333")