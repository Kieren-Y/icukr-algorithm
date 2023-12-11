#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#
# https://leetcode.cn/problems/linked-list-cycle-ii/description/

# 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos
# 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos
# 不作为参数进行传递，仅仅是为了标识链表的实际情况。
#
# 不允许修改 链表。
#
# 示例 1：
# 输入：head = [3,2,0,-4], pos = 1
# 输出：返回索引为 1 的链表节点
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
# 示例 2：
# 输入：head = [1,2], pos = 0
# 输出：返回索引为 0 的链表节点
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
# 示例 3：
# 输入：head = [1], pos = -1
# 输出：返回 null
# 解释：链表中没有环。
#
# 进阶：你是否可以使用 O(1) 空间解决此题？


# @lc code=start
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    - 1.suppose slow has run k steps, fast has run 2k steps
        when fast and slow meet, cycle length is k
    - 2.suppose the distance from meet point to cycle start is m
        the distance from head to cycle start is k-m
        and also the distance from meet point to cycle start is k-m
    so when reset fast pointer to head, move both fast and slow pointer one step each time
    will meet at cycle start
    """

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1.use slow and fast pointer to find the cycle
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        else:
            return None
        # 2. find the cycle start
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next

        return fast


# @lc code=end
