import random as rd 

print("Random number between 0 and 1:", rd.random())
print("Random integer between 1 and 10:", rd.randint(1, 10))
print("Random choice from a list:", rd.choice(['apple', 'banana', 'cherry', 'date']))
print("Random sample of 3 elements from a list:", rd.sample(range(1, 20), 3))
print(rd.randrange(0, 100, 5))  # Random number from 0 to 100 with step of 5