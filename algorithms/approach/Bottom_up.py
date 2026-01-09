#Bottom_up approach
def fibonacci_bottom(n):
    if n <= 1:
        return n
    # create a table to store results of subproblems
    fib_table = [0] * (n + 1)
    fib_table[1] = 1
    # fill the table in a bottom-up manner
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
        print(fib_table[i])
    return fib_table[n]
print(fibonacci_bottom(10))