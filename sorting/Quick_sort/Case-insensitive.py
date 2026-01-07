def quick_sort_case_insensitive(strings):
    if len(strings) <= 1:
        return strings
    else:
        pivot = strings[len(strings) // 2]
        left = [x for x in strings if x.lower() < pivot.lower()]
        middle = [x for x in strings if x.lower() == pivot.lower()]
        right = [x for x in strings if x.lower() > pivot.lower()]
        return quick_sort_case_insensitive(left) + middle + quick_sort_case_insensitive(right)
# Example usage:
strings = ["banana", "Apple", "orange", "apple", "Banana"]
sorted_strings = quick_sort_case_insensitive(strings)
print(sorted_strings)  
# Output: ['Apple', 'apple', 'banana', 'Banana', 'orange']