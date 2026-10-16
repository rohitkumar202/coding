# Backtracking: choose a number, recurse, then undo the choice so the next loop starts clean.
# n! permutations, each copied in O(n) -> O(n * n!) time.
def permutations(nums, container, used, res):
    if len(container) == len(nums):
        res.append(container[:])  # copy: container keeps changing after this
        return
    
    for num in nums:
        if num not in used:  # NOTE: a set of values breaks on duplicate nums; track indices then
            container.append(num)
            used.add(num)
            permutations(nums, container, used, res)
            container.pop()  # undo both changes (backtrack)
            used.remove(num)


if __name__ == "__main__":
    nums = [1, 2, 3]
    res = []
    permutations(nums, [], set(), res)
    print(res)
