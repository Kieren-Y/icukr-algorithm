#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
# https://leetcode.cn/problems/move-zeroes/description/
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
#
# 示例 1:
# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]
#
#
# 示例 2:
# 输入: nums = [0]
# 输出: [0]

#
# 进阶：你能尽量减少完成的操作次数吗？
#
#

# @lc code=start
from typing import List


class Solution:
    def _remove_value(self, nums: List[int], value: int):
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] != value:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = self._remove_value(nums, 0)
        for slow in range(slow, len(nums)):
            nums[slow] = 0


# @lc code=end
