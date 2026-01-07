def sequential_search(nlist,key):
    pos = 0
    found = False

    while pos < len(nlist) and not found:
        if nlist[pos] == key:
            found = True

        else:
            pos = pos + 1
    return found,pos
# Example usage:
numbers = [4, 2, 3, 5, 1]
print(sequential_search(numbers, 3))  # Output: True
print(sequential_search(numbers, 6))  # Output: False