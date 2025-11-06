s = "*"
for i in range(1, 6):
    print(s * i)

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    print(s * i)

for i in range(1, 6):
    print(s * i)
for i in range(5, 0, -1):
    print(s * i)

for i in range(1, 6):
    for j in range(1, i + 1):
        print(s * j, end=" ")
    print()