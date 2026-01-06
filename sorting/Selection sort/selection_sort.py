def selectionsort(nlist):
    for fillslot in range(len(nlist)-1,0,-1):
        maxpos=0
        for location in range(1,fillslot+1):
            if nlist[location]>nlist[maxpos]:
                maxpos=location


        temp = nlist[fillslot]
        nlist[fillslot]=nlist[maxpos]
        nlist[maxpos]=temp


l1 = [54,26,93,17,77,31,44,55,20]
selectionsort(l1)
print("Sorted list is:",l1)