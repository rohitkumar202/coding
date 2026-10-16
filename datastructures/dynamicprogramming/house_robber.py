# Test inputs: only the last assignment is used; swap the order to try another.
arr = [200, 300, 200, 50]      # 400: 200 + 200
arr = [5]                      # 5
arr = [2, 7, 9, 3, 1]          # 12: 2 + 9 + 1
arr = [5, 5, 10, 100, 10, 5]   # 110: 5 + 100 + 5

# House robber: max sum of non-adjacent houses.
# rob(i) = best total from house i onward. Same take-or-skip idea as coin change,
# but taking jumps to i + 2 because the next house is adjacent.
# Plain recursion is exponential (Fibonacci tree); memo on i makes it O(n).
def rob(i, arr):
    if i >= len(arr):
        return 0  # past the last house: nothing left to rob
    
    # take house i and skip its neighbor, or skip house i
    return max(arr[i] + rob(i + 2, arr), rob(i + 1, arr))

    
print(rob(0, arr))


