class Node:
    def __init__(self, val = 0, nextNode = None):
        self.val = val
        self.next = nextNode

class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val, None)
        newNode.next = self.head.next
        self.head.next = newNode
        if not newNode.next:        # If list empty before insertion
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val, None)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next

        return res
        
