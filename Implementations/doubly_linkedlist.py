# Doubly linkedlist implementation

class ListNode:
    def __init__(self,value=0,prev=None,next=None) -> None:
        self.value = value
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self,value) -> None:
        self.dummy = ListNode()
        self.head = ListNode(value)
        self.dummy.next = self.head
        self.head.prev = self.dummy
        self.length = 1

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
        next_node = self.head
        new_node = ListNode(value)
        self.head = new_node

        self.dummy.next = self.head
        self.head.prev = self.dummy

        self.head.next = next_node
        next_node.prev = self.head
        self.length += 1
        return self.head

    # Add at index

    # TC : O(N)
    # SC : O(1)
    def add_at_index(self,index,value):
        if index == 0:
            self.add_at_start(value)
            return
        
        curr = self.dummy
        for _ in range(index):
            curr = curr.next
        next_node = curr.next
        new_node = ListNode(value)

        curr.next = new_node
        new_node.prev = curr

        new_node.next = next_node
        next_node.prev = new_node
        self.length += 1
        return self.head

    
    # Add at end

    # TC : O(N)
    # SC : O(1)
    def add_at_end(self,value):
        curr = self.head
        while curr.next:
            curr = curr.next
        new_node = ListNode(value)
        curr.next = new_node
        new_node.prev = curr
        self.length += 1
        return self.head
    
    # Remove at start

    # TC : O(1)
    # SC : O(1)
    def remove_from_start(self):
        next_node = self.head.next
        self.dummy.next = next_node
        next_node.prev = self.dummy
        self.head = next_node
        self.length -= 1
        return self.head

    # Remove at index

    # TC : O(N)
    # SC : O(1)
    def remove_from_index(self,index):
        if index == 0:
            self.remove_from_start()
            return
        print('self.length ',self.length)
        if index > self.length-1:
            return None
        curr = self.dummy
        for _ in range(index):
            curr = curr.next
        next_node = curr.next.next
        curr.next = next_node
        if next_node:
            next_node.prev = curr
        self.length -= 1
        return self.head
    
    # Remove at end

    # TC : O(N)
    # SC : O(1)
    def remove_from_end(self):
        if self.head.next is None:
            return None
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None
        self.length -= 1
        return self.head
    

ll = LinkedList(2)
ll.add_at_start(1)
ll.add_at_start(0)
ll.add_at_end(3)
ll.add_at_end(5)
ll.add_at_index(4,4)
ll.remove_from_start()
ll.remove_from_index(4)
ll.remove_from_end()
ll.print_linkedlist()

