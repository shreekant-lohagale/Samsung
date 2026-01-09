#find maximun element using daivide and conquer approach
def find_maximum(arr, left, right):
    # Base case: If the array has only one element
    if left == right:
        return arr[left]

    # Find the middle index
    mid = (left + right) // 2

    max_left = find_maximum(arr, left, mid)
    max_right = find_maximum(arr, mid + 1, right)

    return max(max_left, max_right)
# Example usage
l = [3, 1, 8, 9, 2]
print(find_maximum(l, 0, len(l) - 1))
