"""
Two types of coin change problems, solved with the same recursion:
1. ways(): number of ways to make a target sum using the given coins (LeetCode 518)
2. count_coins(): minimum number of coins to make a target sum (LeetCode 322)

Things to remember:
- Each coin can be used unlimited times. At coin i, either take it (stay at i,
  so it can be taken again) or skip it (move to i + 1 and never come back).
- Moving only forward through the coins counts combinations, not orderings:
  1+5 and 5+1 are one way. Looping over all coins at every step would count
  both orders (that's a different problem, LeetCode 377).
- Same recursion, different base cases:
    ways:        target == 0 -> 1 (found one way)      dead end -> 0
    count_coins: target == 0 -> 0 (no more coins)      dead end -> inf
- inf means "impossible" so min() ignores that branch; turn it into -1 at the end.
- Plain recursion is exponential. Memoizing on (i, target) makes it
  O(len(coins) * target) time and space.
- Recursion depth grows with target (coin 1 recurses target times), so a target
  around 1000 hits Python's recursion limit. Use a bottom-up table for big targets.
- Assumes every coin is positive: a 0 coin never shrinks target, so it recurses forever.
"""
coins = [1, 5]
target = 11


# Core logic: plain recursion, exponential time

def ways(coins, i, target):
    if target == 0:
        return 1
    if target < 0 or i >= len(coins):
        return 0

    # take coin i (stay at i to reuse it) + skip coin i for good
    return ways(coins, i, target - coins[i]) + ways(coins, i + 1, target)


def count_coins(coins, i, target):
    if target == 0:
        return 0
    if target < 0 or i >= len(coins):
        return float('inf')

    # taking coin i costs 1 coin; skipping it costs nothing
    return min(1 + count_coins(coins, i, target - coins[i]), count_coins(coins, i + 1, target))


# Memoized: same logic plus a cache on (i, target), O(len(coins) * target)

def ways_memo(coins, i, target, memo=None):
    # None default, not {}: a {} default would be shared across calls
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


def count_coins_memo(coins, i, target, memo=None):
    if memo is None:
        memo = {}
    if target == 0:
        return 0
    if target < 0 or i >= len(coins):
        return float('inf')
    if (i, target) in memo:
        return memo[(i, target)]

    memo[(i, target)] = min(1 + count_coins_memo(coins, i, target - coins[i], memo),
                            count_coins_memo(coins, i + 1, target, memo))
    return memo[(i, target)]


def min_coins(coins, target):
    res = count_coins_memo(coins, 0, target)
    # inf means no combination of coins reaches target
    return -1 if res == float('inf') else res


if __name__ == "__main__":
    print(ways(coins, 0, target))        # 3: 1*11, 5+1*6, 5+5+1
    print(ways_memo(coins, 0, target))   # 3
    print(count_coins(coins, 0, target)) # 3: 5+5+1
    print(min_coins(coins, target))      # 3: 5+5+1
    print(min_coins([2], 3))             # -1: odd target, only even coins
    print(min_coins([1, 2, 5], 0))       # 0: nothing to make
