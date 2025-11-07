breads = ["rye", "sourdough", "pumpernickel", "wheat"]
meats = ["turkey", "ham", "roast beef", "chicken"]
cheeses = ["cheddar", "Swiss", "provolone", "American"]
vegis = ["lettuce", "tomato", "onion", "pickles"]
print("possible sandwich combinations:")

for bread in breads:
    for meat in meats:
        for cheese in cheeses:
            for vegi in vegis:
                print("-", bread, meat, cheese, vegi)

for i in range(10):
    print(i)

li = [1,2,3,4,5,6]
li1 = []
for i in li:
    if i % 2 == 0:
        li1.append(i)
        print(li1)

for i in range(5):
    for j in range(3):
        print(i)

for i in range(1,20):
    print(i * 2)