class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head

    def add(self, key):         #agregar al principio
        nodo = Node(key)
        if not self.isEmpty():
            self.head = nodo
            self.last  = nodo
        else:
            nodo.next = self.head
            self.head = nodo

    def append(self,key):
        nodo = Node(key)
        if not self.isEmpty():
            self.head = nodo
        else:
            self.last.next = nodo
            self.last = nodo

    def print(self):
        i = self.head
        while i:
            print(i.data, end=' -> ')
            i = i.next
        print()

ll = LinkedList()
ll.add(2)
ll.add(3)
ll.add(7)
ll.add(1)
ll.append(6)
ll.append(8)
ll.print()