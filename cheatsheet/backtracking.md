# Backtracking

Code: [permutations.py](../datastructures/backtracking/permutations.py) · [subsets.py](../datastructures/backtracking/subsets.py)

## Important points

- Pattern: choose, recurse, undo. Undo every change you made before the next loop iteration.
- Append a **copy** (`container[:]`). The list keeps changing after you append it.
- Permutations: loop over all nums and skip used ones. n! results, O(n · n!) time.
- Subsets: only pick nums **after** the last pick, else you get every ordering. 2^n results.
- A `used` set of values breaks on duplicate nums. Track indices instead.

## Permutations

```python
def permutations(nums, container, used, res):
    if len(container) == len(nums):
        res.append(container[:])
        return
    for num in nums:
        if num not in used:
            container.append(num)
            used.add(num)
            permutations(nums, container, used, res)
            container.pop()
            used.remove(num)
```

## Problems

| Problem | Pattern | Key trick | Code |
|---|---|---|---|
| Permutations | Choose / recurse / undo | `used` set skips numbers already in `container`. Undo both `container` and `used` after recursing | [permutations.py](../datastructures/backtracking/permutations.py) |
| Subsets | One call per length | **Known bug:** picks from all remaining nums, so `[1, 2]` and `[2, 1]` both appear (16 results, not 8). Fix: only pick nums after the last pick | [subsets.py](../datastructures/backtracking/subsets.py) |
