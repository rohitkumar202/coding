# Two pointers

Code: [two_sum.py](../datastructures/two_pointers/two_sum.py)

## Important points

- Needs a **sorted** array. Unsorted two sum uses a hash map instead (O(n) space).
- Start at both ends. Sum too big → `j -= 1`, too small → `i += 1`.
- Each move drops a number that can't be in any pair, so nothing is missed.
- Loop `while i < j`: a number can't pair with itself.
- O(n) time, O(1) space.

## Two sum (sorted)

```python
def two_sum(nums, target):
    i, j = 0, len(nums) - 1
    while i < j:
        s = nums[i] + nums[j]
        if s == target:
            return [i, j]
        elif s > target:
            j -= 1
        else:
            i += 1
    return [-1, -1]
```

## Problems

| Problem | Pattern | Key trick | Code |
|---|---|---|---|
| Two sum (sorted array) | Pointers from both ends | Too big → move `j` left, too small → move `i` right. No pair when the pointers meet → `[-1, -1]` | [two_sum.py](../datastructures/two_pointers/two_sum.py) |
