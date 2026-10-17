"""
Problem: Given a sorted integer array nums and an integer target, return the indices [i, j] (i < j) of two numbers that add up to target. 
If no pair exists, return [-1, -1]. Solve it in O(n) time and O(1) extra space.
Sample input:
nums = [1, 3, 4, 6, 8, 11]
target = 10

"""

# Two pointers from both ends; works only because nums is sorted.
# Too big -> drop the largest (j - 1), too small -> drop the smallest (i + 1).
# Each step discards a number that can't be in any pair, so no pair is missed: O(n) time, O(1) space.
def two_sum(nums, target):
    i = 0
    j = len(nums) - 1

    while i < j:  # i < j, not <=: a number can't pair with itself
        if nums[i] + nums[j] == target:
            return [i, j]
        
        if nums[i] + nums[j] > target:
            j = j - 1  # nums[j] is too big even with the smallest left, so drop it

        # NOTE: plain `if`, so this sees the new j and both moves can run in one pass.
        #       Still correct (the loop rechecks i < j and the sum), but `elif` is clearer.
        if nums[i] + nums[j] < target:
            i = i + 1  # nums[i] is too small even with the largest left, so drop it

    return [-1, -1]  # pointers met: no pair

if __name__ == "__main__":
    nums = [1, 3, 4, 6, 8, 11]
    target = 13  # [-1, -1]: no pair; target = 10 gives [2, 3] (4 + 6)

    res = two_sum(nums, target)
    print(res)