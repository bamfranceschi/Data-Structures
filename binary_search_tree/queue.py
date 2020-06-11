"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


# class Node:
#     def __init__(self, value=None, next_node=None):
#         # the value at this linked list node
#         self.value = value
#         # reference to the next node in the list
#         self.next_node = next_node​
#     def get_value(self):
#         return self.value
#     def get_next(self):
#         return self.next_node
#     def set_next(self, new_next):
#         # set this node's next_node reference to the passed in node
#         self.next_node = new_next
# ​
# class LinkedList:
#     def __init__(self):
#         # reference to the head of the list
#         self.head = None
#         # reference to the tail of the list
#         self.tail = None

#     def add_to_tail(self, value):
#         # wrap the input value in a node
#         new_node = Node(value, None)
#         # check if there is no head (i.e., the list is empty)
#         if not self.head:
#             # if the list is initially empty, set both head and tail to the new node
#             self.head = new_node
#             self.tail = new_node
#         # we have a non-empty list, add the new node to the tail
#         else:
#             # set the current tail's next reference to our new node
#             self.tail.set_next(new_node)
#             # set the list's tail reference to the new node
#             self.tail = new_node

#     def remove_head(self):
#         # return None if there is no head (i.e. the list is empty)
#         if not self.head:
#             return None
#         # if head has no next, then we have a single element in our list
#         if not self.head.get_next():
#             # get a reference to the head
#             head = self.head
#             # delete the list's head reference
#             self.head = None
#             # also make sure the tail reference doesn't refer to anything
#             self.tail = None
#             # return the value
#             return head.get_value()
#         # otherwise we have more than one element in our list
#         value = self.head.get_value()
#         # set the head reference to the current head's next node in the list
#         self.head = self.head.get_next()
#         return value

#     def remove_tail(self):
#         if not self.head:
#             return None

#         if self.head is self.tail:
#             value = self.head.get_value()
#             self.head = None
#             self.tail = None
#             return value

#         current = self.head
#         while current.get_next() is not self.tail:
#             current = current.get_next()
#         value = self.tail.get_value()
#         self.tail = current
#         self.tail.set_next(None)
#         return value


#     def contains(self, value):
#         if not self.head:
#             return False
#         # Recursive solution
#         # def search(node):
#         #   if node.get_value() == value:
#         #     return True
#         #   if not node.get_next():
#         #     return False
#         #   return search(node.get_next())
#         # return search(self.head)

#         # get a reference to the node we're currently at; update this as we traverse the list
#         current = self.head
#         # check to see if we're at a valid node
#         while current:
#             # return True if the current value we're looking at matches our target value
#             if current.get_value() == value:
#                 return True
#             # update our current node to the current node's next node
#             current = current.get_next()
#         # if we've gotten here, then the target node isn't in our list
#         return False

#     def get_max(self):
#         if not self.head:
#             return None
#         # reference to the largest value we've seen so far
#         max_value = self.head.get_value()
#         # reference to our current node as we traverse the list
#         current = self.head.get_next()
#         # check to see if we're still at a valid list node
#         while current:
#             # check to see if the current value is greater than the max_value
#             if current.get_value() > max_value:
#                 # if so, update our max_value variable
#                 max_value = current.get_value()
#             # update the current node to the next node in the list
#             current = current.get_next()
#         return max_value

"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node is self.head:
            return
        self.add_to_head(node.value)
        self.delete(node)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node is self.tail:
            return
        self.add_to_tail(node.value)
        self.delete(node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = node.next
            node.delete()
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        current = self.head
        max = self.head.value
        while current is not None:
            if current.value > max:
                max = current.value
            current = current.next
        return max


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_from_tail()
