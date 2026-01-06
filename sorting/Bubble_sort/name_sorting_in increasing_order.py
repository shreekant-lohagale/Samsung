#accept the name from the user and arrange them in increasing order using bubble sort
name = []
for i in range(5):
    name.append(input("Enter name:"))

    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    
sorted_names = bubble_sort(name)
print(f"Names in increasing order: {sorted_names}")