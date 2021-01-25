from collections import Counter


def is_permu_1(first, second):
    if len(first) != len(second):
        print("False")
        return False
    s1, s2 = sorted(first), sorted(second)
    print(s1 == s2)
    return s1 == s2


def is_permu_2(first, second):
    if len(first) != len(second):
        print("False")
        return False
    counter = [0] * 256

    for char in first:
        counter[ord(char)] += 1
    for char in second:
        if counter[ord(char)] == 0:
            print("False")
            return False
        counter[ord(char)] -= 1

    print("True")
    return True


def is_permu_3(first, second):
    print(Counter(first) == Counter(second))
    return Counter(first) == Counter(second)


# Test Cases
is_permu_1("123", "321")
is_permu_2("123", "321")
is_permu_3("123", "321")
is_permu_1("332", "123")
is_permu_2("332", "123")
is_permu_3("332", "123")
is_permu_1("3323", "123")
is_permu_2("3323", "123")
is_permu_3("3323", "123")
