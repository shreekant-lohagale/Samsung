#Top-Down DP

def fibonacci_top(n, memo={}):
    if n <= 1:
        return n
    # if aleady compute, return from memo
    if n in memo:
        return memo[n]
    # compute and store in memo
    memo[n] = fibonacci_top(n-1, memo) + fibonacci_top(n-2, memo)
    print(memo[n])
    return memo[n]

print(fibonacci_top(10))