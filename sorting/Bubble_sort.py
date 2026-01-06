def bubble_sort(arr):
    n = len(arr)

    swap_count = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_count += 1
    return swap_count, arr

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
swaps, sorted_numbers = bubble_sort(numbers)
print(f"Sorted array: {sorted_numbers}")
print(f"Total number of swaps: {swaps}")