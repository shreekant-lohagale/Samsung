#insertion sort 
def insertion_sort(l):
    for index in range(1, len(l)):
        current_value = l[index]
        position = index

        while position > 0 and l[position - 1] > current_value:
            l[position] = l[position - 1]
            position -= 1

        l[position] = current_value


l = [12, 11, 13, 5, 6]
insertion_sort(l)
print("Sorted list is:", l)