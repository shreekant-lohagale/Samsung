#Generate all permutations using backtracking algorithms
def permutation(nums):
    result = []

    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            used[i] = True
            path.append(nums[i])

            backtrack(path, used)

            used[i] = False
            path.pop()

    backtrack([], [False] * len(nums))
    return result
# Example usage
nums = [1, 2, 3]
print(permutation(nums))