#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
# https://leetcode.cn/problems/reverse-linked-list-ii/description/
#
# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left  。请你反转从位置 left 到位置 right 的链表节点，返回
# 反转后的链表 。
#
# 示例 1：
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
#
#
# 示例 2：
# 输入：head = [5], left = 1, right = 1
# 输出：[5]

# 进阶： 你可以使用一趟扫描完成反转吗？
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    successor = None

    def reverseN(self, head: Optional[ListNode], n: int):
        """
        reverse the first N of the chain table
        Skill: not to jump into recursion, but to utilize explicit definitions for algorithmic logic.
        """
        if n == 1:
            self.successor = head.next
            return head
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = self.successor
        return last

    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if left == 1:
            # call reverseN to reverse the first N of the chain table
            return self.reverseN(head, right)
        # when left !=1, will let head.next -> head.next
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head


# @lc code=end
