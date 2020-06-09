##
# Linked List
#
# Characteristics
#  - push adds to TAIL
#  - pop removes from TAIL
#  - iterating starts at HEAD ends at TAIL


# property decorator:
# https://docs.python.org/3/library/functions.html#property

##
# ll = LinkedList()
# ll.push(Node("anna"))
# ll.push(Node("mike"))
# ll.push(Node("lyra"))
#
# ll.peek().value => anna
# ll.peek().next.value => mike
# ll.peek().next.next.value => lyra
class LinkedList:
    class Node:
        def __init__(self, value):
            self._value = value
            self._next = None
            self._prev = None

        def __str__(self):
            return f"[{self._value}]"

        @property
        def value(self):
            return self._value

        @property
        def next(self):
            return self._next

        @next.setter
        def next(self, node):
            self._next = node

        @property
        def prev(self):
            return self._prev

        @prev.setter
        def prev(self, node):
            self._prev = node

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        # if self._head is None:
        #     return 0
        # count = 1
        # current_node = self._head

        # while current_node.next:
        #     count += 1
        #     current_node = current_node.next

        return self._size

    def push(self, value):
        self._size += 1
        if self._head is None:
            self._head = LinkedList.Node(value)
        else:
            node = self._head
            while node.next is not None:
                node = node.next
            new_node = LinkedList.Node(value)
            node.next = new_node
            new_node.prev = node

    def peek(self):
        return self._head

    def pop(self):
        if self._head is not None:
            self._size -= 1
            current_node = self._head

            while current_node.next:
                current_node = current_node.next

            current_node.prev.next = None

            current_node.prev = None

            return current_node


# Ultimately you want your node to not know about the data structure that
# holds it. The node is just data, it could be anything. It could be strings,
# it could be numbers, it could be records from a database, etc. Clean design
# means that these things do not need to know about how they're stored.


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return f"{{ 'name': '{self._name}'', 'age': {self._age} }}"

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


ll = LinkedList()
ll.push(Person("Anna", 31))
ll.push(Person("Mike", 38))
ll.push(Person("Lyra", 1.5))

print(ll.peek())
print(len(ll))
print(ll.pop())
print(len(ll))
print(ll.pop())
print(ll.peek())

# print(ll.peek().next)
# print(ll.peek().next.next)
