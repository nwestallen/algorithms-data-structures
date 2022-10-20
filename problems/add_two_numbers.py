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
        carry = 0
        current = l3
        
        while l1 or l2 or carry:

             first_val = l1.val if l1 else 0
             second_val = l2.val if l2 else 0

             total_sum = first_val + second_val + carry 
             partial_sum = total_sum % 10
             carry = total_sum // 10

             current.next = ListNode(partial_sum)
             current = current.next
             l1 = l1.next if l1 else None
             l2 = l2.next if l2 else None
 
        return l3.next

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
