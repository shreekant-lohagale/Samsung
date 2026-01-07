def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = numbers[len(numbers) // 2]
        left = [x for x in numbers if x < pivot]
        middle = [x for x in numbers if x == pivot]
        right = [x for x in numbers if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Example usage:
numbers = [3,6,8,10,1,2,1]
sorted_numbers = quick_sort(numbers)
print(sorted_numbers)  # Output: [1, 1, 2, 3, 6, 8, 10]