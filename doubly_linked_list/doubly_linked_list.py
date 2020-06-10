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
        # create new_node
        new_node = ListNode(value, None, None)
        # check if DLL is empty:
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
        # check if one element

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        if not self.head:
            return None
        if not self.head.next:
            head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return head.value

        if self.head.next:
            head = self.head  # captures value of old head
            self.head.next.prev = (
                None  # removes the prev pointer pointing to old head from new head
            )
            self.head = self.head.next  # transfers head title to next in line
            self.length -= 1
            return head.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length += 1

        else:

            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if not self.head:
            return None
        if self.head is self.tail:
            value = self.head.value  # grab value
            self.head = None  # set head to none
            self.tail = None  # set tail to none
            self.length -= 1  # decrement length
            return value

        value = self.tail.value  # captures value of tail
        self.tail.prev.next = None  # removes next att for penultimate element
        self.tail = self.tail.prev  # title change to new tail
        self.length -= 1  # decrement length
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):

        if not self.head:
            return None

        if self.head is self.tail:
            self.head = node
            self.tail = node

        if node is not self.tail:
            node.next.prev = (
                node.prev
            )  # assigns node's next's prev pointer to node's prev
            node.prev.next = (
                node.next
            )  # assigns node's prev's next pointer to node's next
            node.next = self.head  # assigns node's next to self.head
            self.head = node  # assigns self.head title to node

        if node is self.tail:
            self.tail.prev.next = None  # assigns tail's prev's next to None
            self.tail.prev = (
                None  # assigns tail's prev to None (this might not be necessary?)
            )
            self.tail = self.tail.prev  # assigns tail title to tail's prev
            node.next = self.head  # assigns node's next to self.head
            self.head = node  # assigns self.head title to node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if self.head is None:
            return None

        if self.head is self.tail:
            self.head = node
            self.tail = node

        if node is self.tail:
            self.tail = node

        else:
            value = node.value
            self.delete(node)
            self.add_to_tail(value)

        # if node is self.head:

        #     node.next.prev = None
        #     node.prev = self.tail
        #     self.tail.next = node
        #     self.head = node.next
        #     self.tail = node
        #     self.tail.next = None

        # if node is not self.head:

        #     node.next.prev = node.prev
        #     node.prev.next = node.next
        #     self.tail.next = node
        #     node.prev = self.tail
        #     self.tail = node
        #     self.tail.next = None

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if self.head is None:
            return None

        if self.head is self.tail:
            value = node.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value

        if node is self.head:
            value = self.head.value  # captures value of head
            self.head.next.prev = None  # resets new head next pointer to none
            self.head = self.head.next
            # sets new head title to second el in list (new head)
            self.length -= 1
            return value

        if node is self.tail:
            value = self.tail.value  # captures value of tail
            self.tail.prev.next = None  # sets next pointer of new tail to none
            self.tail = (
                self.tail.prev
            )  # sets new tail title to second to last el in list
            self.length -= 1

        value = node.value
        node.next.prev = node.prev
        node.prev.next = node.next
        self.length -= 1
        return value

    """Returns the highest value currently in the list"""

    def get_max(self):

        if not self.head:
            return None
        if self.head is self.tail:
            return self.head.value

        max_value = self.head.value

        current = self.head.next

        while current:

            if current.value > max_value:
                max_value = current.value

            current = current.next

        return max_value
