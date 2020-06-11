"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from queue import Queue
from stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # make a new BSTNode with our value

        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        if value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        if target == self.value:
            return True

        elif target < self.value:
            if not self.left:
                return False
            elif self.left:
                if self.left.contains(target):
                    return True

        elif target > self.value:
            if not self.right:
                return False
            elif self.right:
                if self.right.contains(target):
                    return True

        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):

        if not self.right:
            max_value = self.value

            return max_value

        elif self.value <= self.right.value:
            max_value = self.right.get_max()

            return max_value

        # if self.right is None:
        #     return self.value
        # else:
        #     return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # lowest number is always the furthest to the left

        # base case?
        if node is None:
            return

        if node.left:
            node.left.in_order_print(node.left)

        print(node.value)

        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):

        cue = Queue()

        cue.enqueue(node)

        while cue.__len__() > 0:

            current = cue.dequeue()

            print(current.value)

            if current.left:
                cue.enqueue(current.left)

            if current.right:
                cue.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):

        # we'll need a stack class here
        st = Stack()
        # start your stack with the root node
        st.push(node)
        # while loop
        while st.__len__() > 0:
            # checks stack size
            current = st.pop()
            # pointer variable
            print(current.value)

            if current.left:
                st.push(current.left)

            if current.right:
                st.push(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
