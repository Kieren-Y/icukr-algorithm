#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/
#
# 给定一个二叉树 root ，返回其最大深度。
#
# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
#
#
# 示例 1：
# 输入：root = [3,9,20,null,null,15,7]
# 输出：3
#
# 示例 2：
# 输入：root = [1,null,2]
# 输出：2
#

# @lc code=start
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution01:
    """
    skill1:  dynamic programming ideas
    - base case: if root is Nono, depth is 0
    - max depth of root = max( max depth of left node, max depth of right node) + 1
    """

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_left = self.maxDepth(root.left)
        max_right = self.maxDepth(root.right)
        return max(max_left, max_right) + 1


class Solution:
    """
    skill2. backtracking algorithm
    for binary tree traverse,
    - 前序位置的代码在刚刚进入一个二叉树节点的时候执行；
    - 后序位置的代码在将要离开一个二叉树节点的时候执行；
    - 中序位置的代码在一个二叉树节点左子树都遍历完，即将开始遍历右子树的时候执行。
    # 摊牌了,重点还是用中文, 中文才是最吊的。

    前序位置是进入一个节点的时候, 后序位置是离开一个节点的时候, depth 记录当前递归到的节点深度
    把 traverse 理解成在二叉树上游走的一个指针，所以当然要这样维护。
    """

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0

        def traverse(root: Optional[TreeNode], depth: int) -> None:
            nonlocal res
            if not root:
                return

            # position of pre order
            depth += 1
            res = max(res, depth)

            traverse(root.left, depth)
            traverse(root.right, depth)

            # position of post order
            depth -= 1

        traverse(root, depth=0)

        return res


# @lc code=end
