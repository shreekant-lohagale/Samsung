#write a function to perform partial selection sort on a floating point list and then verify the sorted order of the list
def insertion_sort_float(l):
    for index in range(1, len(l)):
        current_value = l[index]
        position = index

        while position > 0 and l[position - 1] > current_value:
            l[position] = l[position - 1]
            position -= 1

        l[position] = current_value

def verify_sorted_order(l):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True

l = [12.5, 11.3, 13.7, 5.2, 6.8]
insertion_sort_float(l) 
print("Sorted list is:", l)
print("Is l sorted?", verify_sorted_order(l))

l2 = [3.14, 2.71, 1.41, 1.73, 0.577]
insertion_sort_float(l2)
print("Sorted list is:", l2)
print("Is l2 sorted?", verify_sorted_order(l2))