#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1 

        while start + 1 < end:
            mid = (start + end ) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid 
                
        if nums[start] >= target:
            return start
        elif nums[start] < target <= nums[end]:
            return end
        else:
            return end + 1 

# @lc code=end

