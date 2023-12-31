#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode.cn/problems/reverse-linked-list/description/
#
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
# 示例 1：
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
#
# 示例 2：
# 输入：head = [1,2]
# 输出：[2,1]
#
#
# 进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
#
# @lc code=start
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList_by_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """recursive solution"""
        if not head or not head.next:
            return head
        last = self.reverseList(head.next)
        # let head next node point to head -- reverse A -> B from B -> A.
        head.next.next = head
        # let tail node<origin head> point to None
        head.next = None

        return last

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """iter solution"""
        pre, curr, nxt = None, head, head
        while curr:
            # record next node, otherwise it will be broken.
            nxt = curr.next
            # reverse the direction
            curr.next = pre

            # move the pointer to next node
            pre = curr
            curr = nxt

        return pre


# @lc code=end
