def binary_case_insensitive(arr, target):
    low = 0
    high = len(arr) - 1
    target = target.lower()  # Convert target to lowercase for case-insensitive comparison

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid].lower()  # Convert mid value to lowercase for comparison

        if mid_value == target:
            return True, mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    return False, -1
# Example usage:
strings = ["Apple", "banana", "Orange", "grape", "Pineapple"]
# The list must be sorted for binary search to work correctly
strings.sort(key=lambda s: s.lower())  # Sort the list in a case-insensitive manner
print(binary_case_insensitive(strings, "orange"))  # Output: (True, index)
print(binary_case_insensitive(strings, "Mango"))   # Output: (False, -1)