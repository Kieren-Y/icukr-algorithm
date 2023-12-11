#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode.cn/problems/remove-duplicates-from-sorted-list/description/
#
# 给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。

# 示例 1：
# 输入：head = [1,1,2]
# 输出：[1,2]
#
# 示例 2：
# 输入：head = [1,1,2,3,3]
# 输出：[1,2,3]


# @lc code=start
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # boundary condition
        if not head:
            return head
        # use fast and slow pointer
        fast, slow = head.next, head
        while fast:
            # when value of fast != slow,  mean meeting a new value node
            # let slow point to new value node, and forward to next
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        # Disconnect from repeating elements that follow
        slow.next = None
        return head


# @lc code=end
