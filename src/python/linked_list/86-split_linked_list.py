# [86] 分隔链表
#
# https://leetcode.cn/problems/partition-list/description/
# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
# 你应当 保留 两个分区中每个节点的初始相对位置。
#
# 示例 1：
# 输入：head = [1,4,3,2,5,2], x = 3
# 输出：[1,2,2,4,3,5]


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # virtual node to save value which lt x
        dummy1 = ListNode(-1)
        # virtual node to save value which gte x
        dummy2 = ListNode(-1)
        p1, p2 = dummy1, dummy2
        p = head
        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            # shouldn't move forward p point directly
            # need block the next pointer for each node in original list
            temp = p.next
            p.next = None
            p = temp

        p1.next = dummy2.next

        return dummy1.next
