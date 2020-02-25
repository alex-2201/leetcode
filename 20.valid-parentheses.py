#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        temp = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        if s == '':
            return True

        for i in s:
            stack.append(i)

            if len(stack) > 1:
                if i in temp and stack[-2] == temp[i]:
                    stack.pop()
                    stack.pop()

        return False if stack else True
# @lc code=end

