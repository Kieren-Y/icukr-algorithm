#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#
# https://leetcode.cn/problems/diameter-of-binary-tree/description/
#
# 给你一棵二叉树的根节点，返回该树的 直径 。
#
# 二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。
#
# 两节点之间路径的 长度 由它们之间边数表示。
#
#
#
# 示例 1：
# 输入：root = [1,2,3,4,5]
# 输出：3
# 解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。
#
# 示例 2：
# 输入：root = [1,2]
# 输出：1
#

#

# @lc code=start
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    tips:
        - dimater of one node = max_left_depth + max_right_depth
        - max_depth -> use post order to solve
        - use global variable to record max dimater of all node
    """

    def __init__(self):
        self._diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self._max_depth(root=root)
        return self._diameter

    def _max_depth(self, root: Optional[TreeNode]):
        if not root:
            return 0

        max_left = self._max_depth(root=root.left)
        max_right = self._max_depth(root=root.right)

        # diameter of root as current node
        diamater = max_left + max_right
        # compare with max diameter of root as others node.
        self._diameter = max(self._diameter, diamater)

        return max(max_left, max_right) + 1


# @lc code=end
