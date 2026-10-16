# Ways to climb n stairs taking 1 or 2 steps: last step was 1 or 2, so f(n) = f(n-1) + f(n-2).
# Plain recursion is exponential (Fibonacci tree); memo on n makes it O(n).
def climb_stairs(n):
    if n == 0:
        return 1  # reached the top exactly: one way
    if n < 0:
        return 0  # overshot the top: not a way
    
    return climb_stairs(n - 1) + climb_stairs(n - 2)

res = climb_stairs(5)
print(res)