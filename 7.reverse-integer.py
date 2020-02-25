#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        res = ''
        for i in reversed(x_str):
            res += i
        res = int(res) if x >= 0 else -int(res[:-1])
        if res >= (2 ** 31 -1) or res < -2 ** 31:
            return 0
        else:
            return res
# @lc code=end
