# Finding even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
print('Even numbers are:', even_numbers)

l1 = [10, 23, 45, 66, 78, 90, 33, 21]
l2 = [] 
for i in l1:
    if i % 2 == 0:
        l2.append(i)
print('Even numbers are:', l2)