# Single LinkedList 

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.ref = None

class SLL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insertSLL(self, data, pos):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if pos == 0:
                newNode.ref = self.head
                self.head = newNode
            elif pos == -1:
                newNode.ref = None
                self.tail.ref = newNode
                self.tail = newNode
            else:
                temp = self.head
                i = 0
                while ((i < pos -1) and temp.ref is not None):
                    temp = temp.ref
                    i += 1
                newNode.ref = temp.ref
                temp.ref = newNode

    def printSLL(self):
        temp = self.head
        while (temp.ref is not None):
            print(temp.data, end=" ")
            temp = temp.ref 




sll = SLL()

# Insert nodes at the beginning
sll.insertSLL(1, 0)
sll.insertSLL(2, 0)
sll.insertSLL(3, 0)
sll.printSLL()  # Output: 3 2 1

# Insert nodes at the end
sll.insertSLL(4, -1)
sll.insertSLL(5, -1)
sll.insertSLL(6, -1)
sll.printSLL()  # Output: 3 2 1 4 5 6

# Insert node at a specific position
sll.insertSLL(7, 2)
sll.insertSLL(8, 4)
sll.insertSLL(9, 6)
sll.printSLL()  # Output: 3 2 7 1 8 4 9 5 6

