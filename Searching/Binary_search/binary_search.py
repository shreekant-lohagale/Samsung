def binary_using_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return True, mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False, -1
# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_using_iterative(arr, 5))  # Output: (True, 4)
print(binary_using_iterative(arr, 10)) # Output: (False, -1)