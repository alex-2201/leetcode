#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        def say(m):
            if m == 1:
                return '1'
            
            if m == 2:
                return '11'

            if m == 3:
                return '21'

            pre = say(m - 1) + '0'
            res = ''
            count = 0
            print(pre)

            for j in range(len(pre)):
                count += 1
                if pre[j] != pre[j + 1]:
                    res = res + str(count) + pre[j]
                    count = 0
            return res
            
        return say(n)

# @lc code=end

