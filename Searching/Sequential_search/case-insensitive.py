def case_insensitive(strings, target):
    pos = 0
    found = False

    while pos < len(strings) and not found:
        if strings[pos].lower() == target.lower():
            found = True
        else:
            pos = pos + 1

    return found, pos
# Example usage:
strings = ["Hello", "world", "Python", "Programming"]
print(case_insensitive(strings, "python"))  # Output: (True, 2)
print(case_insensitive(strings, "java"))    # Output: (False, 4)