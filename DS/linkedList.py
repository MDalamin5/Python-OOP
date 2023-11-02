class Node:
    def __init__(self, data = None, next = None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insertInHead(self, data):
        if self.head is None:
            print("LinkList is Empty")
        
        itr = self.head