#0/1 knapsack

items = ["A", "B", "C"]
weights = [1, 3, 4]
values = [15, 20, 30]

#knapsack capacity
capacity = 4

#DP array
dp = [0] * (capacity + 1)

#create dp table 
for i in range(len(items)):
    for w in range(capacity, weights[i] - 1, -1):
        dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

print("Maximum value in Knapsack:", dp[capacity])