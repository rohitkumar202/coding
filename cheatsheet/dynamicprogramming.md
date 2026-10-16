# Dynamic programming

Code: [climb_stairs.py](../datastructures/dynamicprogramming/climb_stairs.py) · [coin_change.py](../datastructures/dynamicprogramming/coin_change.py)

## Important points

- Write the plain recursion first (keep it as its own function), then cache on the arguments that change (`memo[(i, target)]`).
- Plain recursion is exponential; memo makes it O(number of states).
- Use `memo=None` and create `{}` inside. A `{}` default is shared across calls.
- Base cases depend on what you return: count of ways → `1` at the goal, `0` at a dead end. Minimum → `0` at the goal, `inf` at a dead end.
- `inf` keeps impossible branches out of `min()`. Convert it to `-1` at the end.
- Deep recursion (about 1000 levels) hits Python's limit. Use a bottom-up table for big inputs.

## Take or skip recursion

**Core logic (plain recursion)**
```python
def ways(coins, i, target):
    if target == 0:
        return 1
    if target < 0 or i >= len(coins):
        return 0
    return ways(coins, i, target - coins[i]) + ways(coins, i + 1, target)
```

**Memoized (same logic plus a cache on `(i, target)`)**
```python
def ways_memo(coins, i, target, memo=None):
    if memo is None:
        memo = {}
    if target == 0:
        return 1
    if target < 0 or i >= len(coins):
        return 0
    if (i, target) in memo:
        return memo[(i, target)]
    memo[(i, target)] = ways_memo(coins, i, target - coins[i], memo) + ways_memo(coins, i + 1, target, memo)
    return memo[(i, target)]
```

## Problems

| Problem | Pattern | Key trick | Code |
|---|---|---|---|
| Climb stairs | Recursion (Fibonacci) | `f(n) = f(n-1) + f(n-2)`, `f(0) = 1`, `f(<0) = 0` | [climb_stairs.py](../datastructures/dynamicprogramming/climb_stairs.py) |
| Coin change: number of ways | Take or skip, memo on `(i, target)` | Take = stay at `i` (coins reusable), skip = `i + 1`. Moving forward only counts combinations, not orderings | [coin_change.py](../datastructures/dynamicprogramming/coin_change.py) |
| Coin change: minimum coins | Same recursion with `min` | Base case is `0` at `target == 0` (not `1`: that adds a coin to every answer). Dead end → `inf`, return `-1` if the result is `inf` | [coin_change.py](../datastructures/dynamicprogramming/coin_change.py) |
