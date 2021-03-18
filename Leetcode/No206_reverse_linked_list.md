# 206. 反转链表

## 题目
反转一个单链表。 是一个非常经典的题，记得最开始学的时候只记住了迭代解法，递归没太懂。

## 算例
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

## 我的解
- 可用迭代和递归, 迭代复杂度是 O(n), O(1)
```python
# 迭代：设置一个pre，然后对每一个cur，存好cur.next，然后将cur和pre进行反转，迭代到最后

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        if not cur:
            return cur
        while cur:
            next_ = cur.next
            cur.next = pre
            pre = cur
            cur = next_
        return pre
```
