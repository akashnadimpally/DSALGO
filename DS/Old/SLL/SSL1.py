class Node:
    def __init__(self):
        self.head = None
        self.tail = None

class SLL:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    def insertion(self, pos, value):
        n = Node(value)
        if self.head is None:
            self.head = n
            self.next = n
        else:
            if pos == 0:
                self.head = n
                self.next.next = None