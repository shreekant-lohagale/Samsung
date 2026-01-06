#insertion sort 
def insertion_sort(l):
    for index in range(1, len(l)):
        current_value = l[index]
        position = index

        while position > 0 and l[position - 1] > current_value:
            l[position] = l[position - 1]
            position -= 1

        l[position] = current_value


l = ['A', 'f', 'B', 'c', 'o', 'D', 'e']
insertion_sort(l)
print("Sorted list is:", l)

l2 = ['z', 'x', 'y', 'a', 'c', 'b']
insertion_sort(l2)
print("Sorted list is:", l2)

l3 = ['Shreekant', 'prathamesh', 'yash', 'Sumit', 'raj', 'op']
insertion_sort(l3)
print("Sorted list is:", l3)