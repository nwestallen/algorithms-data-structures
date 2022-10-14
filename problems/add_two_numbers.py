#https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other) -> bool:
        if self.val != other.val:
            return False
        else:
            current_self  = self.next
            current_other = other.next
            while current_self.next:
                if current_self.val != current_other.val:
                    return False
                current_self = current_self.next
                current_other = current_other.next
            return True
        

class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    # We traverse through each input linked list and sum their values, substituting 0 if node is not present
    # any value over 10 gets carried over to the next node. This has O(n) time complexity with n being the 
    # max input linked list length

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

#Testing below - create a LinkedList class for testing convenience

class LinkedList:
    def __init__(self, value_list=None):
        self.head = None
        if value_list:
            while value_list:
                current = ListNode(value_list.pop())
                current.next = self.head
                self.head = current
        else:
            self.head = ListNode()

def test_equivalence():
    assert LinkedList([2, 3, 4]).head == LinkedList([2, 3, 4]).head

def test_basic_sum():
    l1 = LinkedList([0, 0, 1]).head
    l2 = LinkedList([5, 4, 2]).head
    assert Solution().addTwoNumbers(l1, l2) == LinkedList([5, 4, 4]).head

def test_carry_sum():
    l1 = ListNode(9)
    l2 = ListNode(5)
    assert Solution().addTwoNumbers(l1, l2) == LinkedList([4, 1]).head

def test_asymmetric_digits():
    l1 = LinkedList([3, 3, 3]).head
    l2 = LinkedList([2, 2]).head
    assert Solution().addTwoNumbers(l1, l2) == LinkedList([5, 5, 3]).head

def test_multiple_carries():
    l1 = LinkedList([9, 9, 9, 9, 9, 9, 9, 9, 9]).head
    l2 = ListNode(9)
    assert Solution().addTwoNumbers(l1, l2) == LinkedList([8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]).head
