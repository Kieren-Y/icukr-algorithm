#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# https://leetcode.cn/problems/reverse-nodes-in-k-group/description/
#
# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
#
# 示例 1：
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
#
# 示例 2：
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
#
# 进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？
#

# @lc code=start
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# The `Solution` class provides methods to reverse a linked list from a given node range and to
# reverse a linked list in groups of a given size.
class Solution:
    """
    Skill:
    - 1.find base case
    - 2.find the interval of K
    - 3.write a function to reverse linked list from left node to right node
    - 4.let tail node of pre interval linked list point to next interval linkedlist
    """

    def reverse(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        """reverse linked list from node left to node right"""
        pre, curr, ntx = None, left, left
        # left open right close
        while curr != right:
            ntx = curr.next
            curr.next = pre
            pre = curr
            curr = ntx
        return pre

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        # find the interval of k<leftm  right>
        a, b = head, head
        for i in range(k):
            # if not b, meaning move to end of linkedlist
            # return left
            if not b:
                return a
            b = b.next

        new_head = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)

        return new_head


# @lc code=end
