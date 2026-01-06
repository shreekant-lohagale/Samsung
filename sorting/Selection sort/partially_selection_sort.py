#write a function to perform selection sort and output the partially sorted list after ccomlete pass
def partially_selection_sort(nlist):
    for fillslot in range(len(nlist)-1,0,-1):
        maxpos=0
        for location in range(1,fillslot+1):
            if nlist[location]>nlist[maxpos]:
                maxpos=location


        temp = nlist[fillslot]
        nlist[fillslot]=nlist[maxpos]
        nlist[maxpos]=temp
        print(f"List after pass {len(nlist)-fillslot}: {nlist}")

# Example usage
l1 = [64, 25, 12, 22, 11]
partially_selection_sort(l1)
print("Final sorted list is:",l1)
