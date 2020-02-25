#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0

    
        if needle in haystack:
            for j in range(len(haystack)):
                if haystack[j:j + len(needle)] == needle:
                    return j
        
        # i = 0
        # sl = len(needle)
        # while i < len(haystack)- sl + 1:  
        #     if haystack[i] == needle[0]:
        #         sub = haystack[i:i + sl]
        #         if sub == needle:
        #             return i
        #     i += 1
        
        return -1

# @lc code=end

