def binary_search_recursive(arr, target, low, high):
    if low > high:
        return False, -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return True, mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1) 
    
# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search_recursive(arr, 5, 0, len(arr) - 1))  # Output: (True, 4)
print(binary_search_recursive(arr, 10, 0, len(arr) - 1)) # Output: (False, -1)