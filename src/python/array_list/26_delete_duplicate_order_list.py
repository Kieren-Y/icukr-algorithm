#
# @lc app=leetcode.cn id=26 lang=python3

# [26] 删除有序数组中的重复项
#
# https://leetcode.cn/problems/remove-duplicates-from-sorted-array/description/
#
# 给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致.
# 由于在某些语言中不能改变数组的长度，所以必须将结果放在数组nums的第一部分。更规范地说，如果在删除重复项之后有 k 个元素，那么 nums 的前 k
# 个元素应该保存最终结果。
#
# 将最终结果插入 nums 的前 k 个位置后返回 k 。
# 不要使用额外的空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
#
# 示例 1：
# 输入：nums = [1,1,2]
# 输出：2, nums = [1,2,_]
# 解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
#
# 示例 2：
# 输入：nums = [0,0,1,1,1,2,2,3,3,4]
# 输出：5, nums = [0,1,2,3,4]
# 解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4
# 。不需要考虑数组中超出新长度后面的元素。
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # boundary condition
        if len(nums) <= 1:
            return len(nums)
        # use fast and slow pointer
        fast, slow = 1, 0
        while fast < len(nums):
            # when slow != fast, forward slow pointer, and align new value to slow
            # to keep non-repeating values before slow pointer
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1

        return slow + 1


# @lc code=end
