"""
Problem:
You’re given an m × n grid (matrix). You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m-1, n-1). At each step you can move only right or down.

Return the total number of distinct paths from the start to the destination.

Example:

Input: m = 3, n = 3
Output: 6
Input: m = 3, n = 7
Output: 28

Constraints (typical):

1 ≤ m, n ≤ 100
The answer fits in a 32-bit or 64-bit integer, or you’re asked to return it modulo 10^9 + 7.
"""

# paths(r, c) = paths going down + paths going right; every path starts with one of the two.
# Plain recursion is exponential, too slow for 100 x 100. Memo on (r, c) makes it O(m * n).
def matrix_pathway(r, c, m, n):
    if not 0 <= r < m:
        return 0  # stepped off the grid: not a path
    if not 0 <= c < n:
        return 0
    
    if r == m - 1 and c == n - 1:
        return 1  # reached the bottom-right: one path

    return matrix_pathway(r + 1, c, m, n) + matrix_pathway(r, c + 1, m, n)

if __name__ == "__main__":
    m = 3
    n = 7
    print(matrix_pathway(0, 0, m, n))