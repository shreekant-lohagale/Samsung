# i = 1

# while i < 5:
#     print(i)
#     i += 1

# while i < 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1

# while i < 10:
#     if i == 5:
#         i += 1
#         continue
#     print(i)
#     i += 1

n = int(input("Enter a number to sum up to :"))
s = 0
i = 1
while i <= n:
    s = s + i
    i += 1
print('sum of 1 to {} is: {}'.format(n, s))
