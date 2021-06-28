#https://leetcode.com/problems/add-two-numbers/submissions/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode()
        cur1 = l1
        cur2 = l2
        cur3 = l3
        carry = 0
        
        while cur1 or cur2:
            if cur1:
                val1 = cur1.val
                cur1 = cur1.next
            else: 
                val1 = 0
            if cur2:
                val2 = cur2.val
                cur2 = cur2.next
            else:
                val2 = 0
            sum = val1 + val2 + cur3.val
            cur3.val = sum % 10
            carry = sum // 10
            if cur1 or cur2 or carry > 0:
                cur3.next = ListNode(carry)
                cur3 = cur3.next
            
    
        return l3