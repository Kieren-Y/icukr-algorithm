#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#
# https://leetcode.cn/problems/find-largest-value-in-each-tree-row/description/
#
# 给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。
#
# 示例1：
# 输入: root = [1,3,2,5,3,null,9]
# 输出: [1,3,9]
#
#
# 示例2：
# 输入: root = [1,2,3]
# 输出: [1,3]
#
#


# @lc code=start
from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res

        q = deque()
        q.append(root)

        while q:
            level_max_val = float("-inf")
            for _ in range(len(q)):
                curr = q.popleft()
                level_max_val = max(curr.val, level_max_val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(level_max_val)

        return res


# @lc code=end
