# 2. 两数相加

## 题目
给两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字0 之外，这两个数都不会以 0 开头

## 算例
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807

## 我的解
- 一次通过，72ms， 只超过57%
- 原因：我进入一个思想误区，不需要还原两个数字具体是多少。（由于是逆序存储的）
``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        len1 = 0
        len2 = 0
        val1 = 0
        val2 = 0
        while l1:
            
            val1 += l1.val * 10 ** len1
            len1 += 1
            l1 = l1.next
        while l2:
            
            val2 += l2.val * 10 ** len2 
            len2 += 1
            l2 = l2.next
        val = val1 + val2
        len_ = max(len1, len2)

        l = ListNode(val % 10)
        cur = l
        for i in range(len_):
            if val//10 != 0:
                val = val//10
                cur.next = ListNode(val % 10)
                cur = cur.next
            else:
                break
        return l
```

