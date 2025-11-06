num = int(input("Enter a number: "))
if num % 5 == 0:
    print(f"{num} is a multiple of 5.")
else:
    print(f"{num} is not a multiple of 5.")

num2 = int(input("Enter another number: "))
if num2 % 3 == 0 and num2 % 5 == 0:
    print(f"{num2} is a multiple of 3 and 5.")
else:
    print(f"{num2} is not a multiple of 3 and 5.")