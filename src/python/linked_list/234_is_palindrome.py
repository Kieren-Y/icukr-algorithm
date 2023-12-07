#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# https://leetcode.cn/problems/palindrome-linked-list/description/
#
# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
#
# 示例 1：
# 输入：head = [1,2,2,1]
# 输出：true
#
# 示例 2：
# 输入：head = [1,2]
# 输出：false
#
# 进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
#

# @lc code=start
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionByTraverse:
    left: Optional[ListNode] = None

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.left = head
        return self.traverse(head)

    def traverse(self, right: Optional[ListNode]) -> bool:
        # base case
        if not right:
            return True

        res = self.traverse(right.next)
        # Posterior traversal
        # Equivalent to putting the nodes on the stack one by one
        # and then comparing them to the left one by one
        res = res and (self.left.val == right.val)
        self.left = self.left.next

        return res


class Solution:
    left: Optional[ListNode] = None

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # pre/curr/nxt -- save pre / current/ next node
        pre, curr, nxt = None, head, head
        while curr:
            # save next node to nxt, avoid breakage
            nxt = curr.next
            # reverse direction
            curr.next = pre
            # move pre and curr pointer
            pre = curr
            curr = nxt
        return pre

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find mid node
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        if fast:
            # The case of odd numbers
            slow = slow.next

        # rervese linke list which after mid node
        left = head
        right = self.reverse(slow)

        # juge if is palindrome
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


# @lc code=end
