#Sum of all elements using daivide and conquer
def find_sum(arr, left, right):
    # Base case: If the array has only one element
    if left == right:
        return arr[left]

    # Find the middle index
    mid = (left + right) // 2

    sum_left = find_sum(arr, left, mid)
    sum_right = find_sum(arr, mid + 1, right)

    return sum_left + sum_right
# Example usage
l = [3, 1, 8, 9, 2]
print(find_sum(l, 0, len(l) - 1))