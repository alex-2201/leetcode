#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        index = 0
        for char in strs[0]:
            for string in strs[1:]:
                if index == len(string) or char != string[index]:
                    return strs[0][:index]                    
            index += 1

        return strs[0]

# @lc code=end

