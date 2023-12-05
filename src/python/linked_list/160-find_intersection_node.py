#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#
# https://leetcode.cn/problems/intersection-of-two-linked-lists/description/
#
# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

# 示例 1：
# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2,
# skipB = 3
# 输出：Intersected at '8'
# 解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
# 从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,6,1,8,4,5]。
# 在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
# — 请注意相交节点的值不为 1，因为在链表 A 和链表 B 之中值为 1 的节点 (A 中第二个节点和 B 中第三个节点)
# 是不同的节点。换句话说，它们在内存中指向两个不同的位置，而链表 A 和链表 B 中值为 8 的节点 (A 中第三个节点，B 中第四个节点)
# 在内存中指向相同的位置。
#
#
# 进阶：你能否设计一个时间复杂度 O(m + n) 、仅用 O(1) 内存的解决方案？
#
#

# @lc code=start
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    step1: in the beginning, pa points to headA, pb points to headB

    step2: pa and pb move one step forward at the same time,
           if pa reaches the end of listA, it points to headB,
           if pb reaches the end of listB, it points to headA

    step3: if the lists have intersection, will meet at the intersection,
            because pa and pb have the same distance to the intersection
    """

    def getIntersectionNodebyHashmap(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        setA = set()
        p1, p2 = headA, headB
        while p1:
            setA.add(p1)
            p1 = p1.next

        while p2:
            if p2 in setA:
                return p2
            p2 = p2.next

        return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa


# @lc code=end
