def coin_change(coins, amount):
    coins.sort(reverse=True)
    result = []

    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    
    return result

print(coin_change([1, 5, 10, 25], 63))
print(coin_change([1, 5, 10, 20], 100))

#make the change with largest coin 
def large_coin(amount):
    coins = [25, 10, 5, 1]

    count = 0

    for coin in coins:
        count += amount // coin
        amount %= coin
        print(amount)

    return count

print(large_coin(63))