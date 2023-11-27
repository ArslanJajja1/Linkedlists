# Implementation of the singly linkedlist

# ListNode
class ListNode:
    def __init__(self,value=0,next=None) -> None:
        self.value = value
        self.next = next

# Linkedlist

class Linkedlist:
    def __init__(self,value) -> None:
        self.dummy = ListNode()
        self.head = ListNode(value)
        self.dummy.next = self.head
    
    # Print Linkedlist
    def print_linkedlist(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next

    # Add at start

    # TC : O(N)
    # SC : O(1)
    def add_at_start(self,value):
        next_node = self.dummy.next
        new_node = ListNode(value)
        self.head = new_node
        self.dummy.next = self.head
        self.head.next = next_node
        return self.head

    # Add at index

    # TC : O(N)
    # SC : O(1)
    def add_at_index(self,index,value):
        if index == 0:
            self.add_at_start(value)
            return
        curr = self.head
        for _ in range(index):
            curr = curr.next
        next_node = curr.next
        curr.next = ListNode(value)
        curr.next.next = next_node
        return self.head


    # Add at end

    # TC : O(N)
    # SC : O(1)
    def add_at_end(self,value):
        curr = self.dummy
        while curr.next:
            curr = curr.next
        curr.next = ListNode(value)
        return self.head
    
    # Remove from start

    # TC : O(1)
    # SC : O(1)
    def remove_from_start(self):
        self.dummy.next = self.head.next
        self.head = self.dummy.next
        return self.head
    
    # Remove from index

    # TC : O(N)
    # SC : O(1)
    def remove_from_index(self,index):
        if index == 0:
            self.remove_from_start()
            return
        curr = self.dummy
        for _ in range(index):
            curr = curr.next
        curr.next = curr.next.next
        return self.head
        
    # Remove from end

    # TC : O(N)
    # SC : O(1)
    def remove_from_end(self):
        curr = self.dummy

        while curr.next.next:
            curr = curr.next
        curr.next = None
        return self.head
    
    # 1 - 2 - 3 - 4 - 5 - 6
ll = Linkedlist(1)
ll.add_at_end(2)
ll.add_at_end(3)
ll.add_at_end(5)
ll.add_at_end(6)
ll.add_at_start(0)
ll.add_at_index(3,4)
ll.add_at_end(7)
ll.remove_from_start()
ll.remove_from_index(3)
ll.remove_from_end()
ll.print_linkedlist()
