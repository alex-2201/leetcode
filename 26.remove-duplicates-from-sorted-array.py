#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums[:] = sorted(list(set(nums)))
        # return len(nums)
        
        i = 0
        for j in range(1,len(nums)):
            if nums[j] == nums[i]:
                continue
            else:
                i = i+1
                nums[i] = nums[j]
        return i+1
            
# @lc code=end

