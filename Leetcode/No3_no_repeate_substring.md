# 3. 无重复字符的最长子串

## 题目
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

## 算例
输入: s = "abcabcbb"

输出: 3 

解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

## 我的解
- hash表、滑动窗口。 
```python
# 遇到次数就要想到hash表，遇到子串就要想到滑动窗口。就是不断的比较更新子串的起始位置，更新长度。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dic = {}
        max_length = 0 
        left = 0

        for i, char in enumerate(s):
            if char in char_dic:
                left = max(left, char_dic[char] + 1)
                
            char_dic[char] = i
            max_length = max(max_length, i - left + 1)
        return max_length
```
