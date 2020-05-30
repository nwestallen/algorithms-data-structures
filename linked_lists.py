class linked_list_node:
    def __init__(self, val):
        self.val = val
        self.next = None

class linked_list:
    def __init__(self, head):
        self.head = linked_list_node(head)

    def append(self, val):
        walk = self.head
        while walk.next:
            walk = walk.next
        walk.next = linked_list_node(val)
    
    def print(self):
        walk = self.head
        while walk:
            print(walk.val)
            walk = walk.next

    def delete(self, val):
        if self.head.val == val:
            self.head = self.head.next
            return

        walk = self.head
        while walk:
            if walk.next.val == val:
                walk.next = walk.next.next
                return
            walk = walk.next

    def reverse(self):
        prev = None
        curr = self.head
        nxt = self.head.next

        while curr:
            curr.next = prev
            prev = curr
            curr = nxt
            if nxt:
                nxt = nxt.next
        self.head = prev

my_linked_list = linked_list(4)
my_linked_list.append(3)
my_linked_list.append(6)

my_linked_list.print()
print()
my_linked_list.delete(6)
my_linked_list.print()
print()
my_linked_list.append(7)
my_linked_list.append(8)
my_linked_list.print()
print()
my_linked_list.reverse()
my_linked_list.print()
