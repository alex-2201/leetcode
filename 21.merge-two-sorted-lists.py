#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None

        res_node = ListNode(0)
        origin_node = res_node
        
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                res_node.val = l1.val
                l1 = l1.next
            else:
                res_node.val = l2.val
                l2 = l2.next
                
            res_node.next = ListNode(0)
            res_node = res_node.next

        while l1 != None:
            res_node.val = l1.val
            l1 = l1.next
            if l1 != None:
                res_node.next = ListNode(0)
                res_node = res_node.next

        while l2 != None:
            res_node.val = l2.val
            l2 = l2.next
            if l2 != None:
                res_node.next = ListNode(0)
                res_node = res_node.next
        
        # res_node = ListNode(0)
        # print(res_node.val)
        # print(res_node)
        # print(l1.val, l2.val)
        return origin_node
# @lc code=end

