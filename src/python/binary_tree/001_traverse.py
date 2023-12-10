from typing import Optional, List
from abc import ABCMeta, abstractmethod

"""
Note(labuladong):
# 总结得很棒！！！
https://labuladong.github.io/algo/di-ling-zh-bfe1b/dong-ge-da-334dd/

后序位置的特殊之处
说后序位置之前，先简单说下中序和前序。

 - 中序位置主要用在 BST 场景中，你完全可以把 BST 的中序遍历认为是遍历有序数组。
 - 前序位置本身其实没有什么特别的性质，之所以你发现好像很多题都是在前序位置写代码，实际上是因为我们习惯把那些对前中后序位置不敏感的代码写在前序位置罢了。
你可以发现，前序位置的代码执行是自顶向下的，而后序位置的代码执行是自底向上的：
这不奇怪，因为本文开头就说了前序位置是刚刚进入节点的时刻，后序位置是即将离开节点的时刻。

*但这里面大有玄妙*
    - *意味着前序位置的代码只能从函数参数中获取父节点传递来的数据*，
    - *而后序位置的代码不仅可以获取参数数据，还可以获取到子树通过函数返回值传递回来的数据*。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BaseOrder(metaclass=ABCMeta):
    @abstractmethod
    def _traverse(self, root: Optional[TreeNode], res: List[int] = []):
        pass

    def traverse(root: Optional[TreeNode]):
        res = []
        set._traverse(root, res=res)
        return res


class PreOrder(BaseOrder):
    def _traverse(self, root: Optional[TreeNode], res: List[int] = []):
        if not root:
            return
        res.append(root.val)
        self._traverse(root.left, res=res)
        self._traverse(root.right, res=res)


class InOrder(BaseOrder):
    def _traverse(self, root: Optional[TreeNode], res: List[int]):
        if not root:
            return
        self._traverse(root.left, res=res)
        res.append(root.val)
        self._traverse(root.right, res=res)


class PostOrder(BaseOrder):
    def _traverse(self, root: Optional[TreeNode], res: List[int]):
        if not root:
            return
        self._traverse(root.left, res=res)
        self._traverse(root.right, res=res)
        res.append(root.val)


# 如何理解：
# - 前序位置的代码只能从函数参数中获取父节点传递来的数据
# - 后序位置的代码不仅可以获取参数数据，还可以获取到子树通过函数返回值传递回来的数据
# 两个简单的问题：
# 1、如果把根节点看做第 1 层，如何打印出每一个节点所在的层数？
# 2、如何打印出每个节点的左右子树各有多少节点？

# 解答：
# 这两个问题的根本区别在于：
# 一个节点在第几层，你从根节点遍历过来的过程就能顺带记录，用递归函数的参数就能传递下去；
# 而以一个节点为根的整棵子树有多少个节点，你需要遍历完子树之后才能数清楚，然后通过递归函数的返回值拿到答案。


def printLevel(root: Optional[TreeNode]):
    def inner(root: Optional[TreeNode], level: int):
        if not root:
            return
        print(f"{root} node -- in {level} level")
        inner(root.left, level=level + 1)
        inner(root.right, level=level + 1)

    inner(root, level=1)


def printCount(root: Optional[TreeNode]):
    if not root:
        return 0

    left_count = printCount(root.left)
    right_count = printCount(root.right)

    print(f"node {root} have left tree node {left_count} and right tree node {right_count}.")

    return left_count + right_count + 1
