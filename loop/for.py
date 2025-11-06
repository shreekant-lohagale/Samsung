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

