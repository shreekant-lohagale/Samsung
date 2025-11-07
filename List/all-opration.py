l1 = [10, 23, 45, 66, 78, 90, 33, 21]
l2 = [1, 2]

#append
for i in l1:
    if i % 2 == 0:
        l2.append(i)
print('Even numbers are:', l2)

#extend
l3 = [2,4,3,5]
l3.extend(l1)
print('Extended list is:', l3)

#sort
print(l1)
l1.sort()
print(l1)

#reverse
print(l2)
l2.reverse()
print(l2)

#pop
print(l3)
l3.pop()
print(l3)

#remove
print(l1)
l1.remove(10)
print(l1)

string = "beutiful"
if 'a' and 'A' in string:
    print("t is present in the string")
elif 'e' and 'E' in string:
    print("e is present in the string")
elif 'i' and 'I' in string:
    print("i is present in the string")
elif 'o' and 'O' in string:
    print("o is present in the string")
elif 'u' and 'U' in string:
    print("u is present in the string")
else:
    print("no vowel is present in the string")