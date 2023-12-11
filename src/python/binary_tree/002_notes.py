# Notes:

# DFS 算法和回溯算法非常类似，只是在细节上有所区别。
# 这个细节上的差别是什么呢？
# * 其实就是「做选择」和「撤销选择」到底在 for 循环外面还是里面的区别，DFS 算法在外面，回溯算法在里面。*
"""
回溯算法、DFS算法、动态规划三种经典的算法思想,联系以及区别：
动归/DFS/回溯算法都可以看做二叉树问题的扩展，只是它们的关注点不同：

- # * 动态规划算法属于分解问题的思路，它的关注点在整棵「子树」*。
- # * 回溯算法属于遍历的思路，它的关注点在节点间的「树枝」。
- # * DFS 算法属于遍历的思路，它的关注点在单个「节点」。

"""

# code
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def counter(root: Optional[TreeNode]):
    # * 1.动态规划, 案例解析
    # * 着眼点永远是结构相同的整个子问题，类比到二叉树上就是「子树」。
    if not root:
        return 0
    left_count = counter(root=root.left)
    right_count = counter(root=root.right)

    return left_count + right_count + 1


class Node:
    def __init__(self, val: int, children: List["Node"]):
        self.val = val
        self.children = children


def printTree(root: Node) -> None:
    # * 2.回溯算法, 案例解析
    # * 遍历的思路，它的着眼点永远是在节点之间移动的过程，类比到二叉树上就是「树枝」。
    if root is None:
        return
    for child in root.children:
        print(f"from node {root} enter to node {child}")
        printTree(child)
        print(f"from node {child} back to {root}")


def add_tree_value(root: TreeNode) -> None:
    # * 3.DFS 算法, 案例解析
    # * 遍历的思路，它的着眼点永远是在单一的节点上，类比到二叉树上就是处理每个「节点」。
    if root is None:
        return
    root.val += 1
    add_tree_value(root.left)
    add_tree_value(root.right)


# 总结：
# -动态规划关注整棵「子树」，回溯算法关注节点间的「树枝」，DFS 算法关注单个「节点」。
# - DFS 算法把「做选择」「撤销选择」的逻辑放在 for 循环外面。
# - 回溯算法必须把「做选择」和「撤销选择」的逻辑放在 for 循环里面，否则怎么拿到「树枝」的两个端点。
