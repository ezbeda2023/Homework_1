def find_dup_str(s, n):
    if n <= 0:
        return ""

    for first_start in range(len(s) - n + 1):
        substring = s[first_start:first_start + n]

        for second_start in range(first_start + n, len(s) - n + 1):
            if s[second_start:second_start + n] == substring:
                return substring

    return ""


def find_max_dup(s):
    for length in range(len(s) // 2, 0, -1):
        duplicated = find_dup_str(s, length)
        if duplicated != "":
            return duplicated

    return ""


# Test part (a).
text = input("Enter a string: ")
length = int(input("Enter a substring length: "))
print(find_dup_str(text, length))

# Test part (b).
text = input("Enter a string: ")
print(find_max_dup(text))
