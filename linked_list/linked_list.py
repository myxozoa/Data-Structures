"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        if not self.tail:
            self.tail = node
        else:
            self.tail.set_next(node)
            self.tail = node

    def remove_head(self):
        if self.head == None:
            self.tail = None
            return None
        popped = self.head.value
        self.head = self.head.get_next()
        return popped

    def contains(self, target):
        current = self.head
        while not current == None:
            if current.value == target:
                return True
            current = current.get_next()
        return False

    def get_max(self):
      if self.head == None:
        return None
      current = self.head
      max = self.head
      while not current == None:
        if current.value > max.value:
          max = current
        current = current.get_next()
      return max.value
