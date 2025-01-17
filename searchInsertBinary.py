"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
"""
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        right = len(nums) - 1
        left = 0

        while(right >= left):
            mid = (right+left)//2
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return left