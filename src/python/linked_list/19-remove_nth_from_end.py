#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/
#
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
#
# 示例 1：
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
#
# 示例 2：
# 输入：head = [1], n = 1
# 输出：[]
#
# 进阶：你能尝试使用一趟扫描实现吗？


# @lc code=start
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd01(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        # Create a dummy node to handle the edge case where the head node is removed
        dummy = ListNode(val=-1, next=head)
        fast = dummy
        slow = dummy
        step = 0
        while fast.next:
            if step < n:
                # let fast pointer move n steps first
                step += 1
            else:
                # after fast pointer move n steps, let slow pointer and fast pointer move together
                slow = slow.next
            fast = fast.next
        # delete the nth node from this linked list
        slow.next = slow.next.next

        return dummy.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        # Create a dummy node to handle the edge case where the head node is removed
        dummy = ListNode(val=-1, next=head)
        fast = dummy
        slow = dummy
        step = 0

        # let fast pointer move n steps first
        while fast and step < n:
            fast = fast.next
            step += 1

        # if n is greater than the length of the linked list, raise ValueError.
        if step < n:
            raise ValueError("n is greater than the length of the linked list")

        # let slow pointer and fast pointer move together until fast pointer reaches the end of the linked list
        while fast.next:
            fast = fast.next
            slow = slow.next

        # remove the nth node from this linked list
        slow.next = slow.next.next

        return dummy.next


# @lc code=end
