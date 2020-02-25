#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums[:] = [x for x in nums if x != val]
        # return len(nums)

        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count +=1
        return count

        # for i in range(nums.count(val)):
	    #     nums.remove(val)
        # return len(nums)
# @lc code=end

