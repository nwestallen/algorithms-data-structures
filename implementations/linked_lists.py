class LinkedList:

    def __init__(self, head = None):
        if head:
            self.head = ListNode(head)
        else:
            self.head = None

    def __str__(self) -> str:
        list_text = 'HEAD -> '
        current = self.head
        while current:
            list_text += str(current.value) + ' -> '
            current = current.next
        list_text += 'None'
        return list_text

    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            else:
                current = current.next
        return
    
    def add(self, value):
        node = ListNode(value)
        node.next = self.head
        self.head = node

    def remove(self, value):
        current = self.head
        previous = None
        while current:
            if current.value == value:
                if previous == None:
                    self.head == self.head.next
                    return
                else:
                    previous.next = current.next
            else:
                previous = current
                current = current.next
        raise ValueError('no node with value ' + str(value) + ' found in list')

class ListNode:
    
    def __init__(self, value):
        self.value = value
        self.next = None