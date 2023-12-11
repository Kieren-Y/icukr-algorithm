#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode.cn/problems/longest-palindromic-substring/description/
#
# 给你一个字符串 s，找到 s 中最长的回文子串。
#
# 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
#
#
# 示例 1：
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#
# 示例 2：
# 输入：s = "cbbd"
# 输出："bb"
#


# @lc code=start
class Solution:
    def find_palindrome(self, s: str, l: int, r: int) -> str:
        # 边界条件，防止越界
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # 以 l, r为中心，不断往外扩展
            l -= 1
            r += 1
        return s[l + 1 : r]

    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # 单节点位中心点的最长回字文
            s1 = self.find_palindrome(s, l=i, r=i)
            # 双节点为中心点的最长回字文
            s2 = self.find_palindrome(s, l=i, r=i + 1)

            # 三者之间取其长
            res = res if len(res) >= len(s1) else s1
            res = res if len(res) >= len(s2) else s2

        return res


# @lc code=end
