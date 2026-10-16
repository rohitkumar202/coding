# Builds every list of length `ln` from nums, called once per length 0..len(nums).
# NOTE: this gives every ordering, not subsets: [1, 2] and [2, 1] both appear (16 results
#       for [1, 2, 3], expected 2^3 = 8). For subsets, only pick nums after the last pick,
#       e.g. recurse on nums[k + 1:] for the k-th num. `used` is never read, so it can go.
def subsets(ln, nums, container, used, res):
    if ln == len(container):
        res.append(container[:])  # copy: container keeps changing after this
        return

    for num in nums:
        container.append(num)
        used.add(num)
        new = [*nums]
        new.remove(num)  # remaining nums, so a num isn't picked twice
        subsets(ln, new, container, used, res)
        container.pop()  # backtrack
        #used.remove(num)

            
            


if __name__ == "__main__":
    nums = [1, 2, 3]
    res = []

    for ln in range(len(nums) + 1):
        subsets(ln, nums, [], set(), res)

    print(res)
    
    