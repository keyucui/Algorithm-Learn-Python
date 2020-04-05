"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.

"""

"""
思路1：循环，每一层得到的和数，再进入一层循环，用除和取余来得到每一位数之和。 注意每一层循环之后，和得重置为0
"""

class Solution:
    def addDigits(self, num: int) -> int:
        x = 0
        while 1:
            while num/10 >= 1:
                x += num%10
                num //= 10
            x += num
            if x < 10:
                return x
            else:
                num = x
                x = 0
