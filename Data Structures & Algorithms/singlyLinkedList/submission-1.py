class _Node:

    def __init__(self, data):
        self.value = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = _Node(-1)
        self.tail = self.head


    def get(self, index: int) -> int:
        i = 0
        curr_node = self.head.next

        while curr_node != None:
            if i == index:
                return curr_node.value
            curr_node = curr_node.next
            i += 1

        return -1


    def insertHead(self, val: int) -> None:
        prev_head = self.head.next
        self.head.next = _Node(val)
        self.head.next.next = prev_head


    def insertTail(self, val: int) -> None:
        curr_node = self.head

        while curr_node.next != None:
            curr_node = curr_node.next
        
        curr_node.next = _Node(val)
        self.tail = curr_node.next
        

    def remove(self, index: int) -> bool:
        i = 0
        curr_node = self.head.next
        prev_node = self.head

        while curr_node != None:
            if i == index:
                prev_node.next = curr_node.next
                return True
            prev_node = curr_node
            curr_node = curr_node.next
            i += 1

        return False

    def getValues(self) -> List[int]:
        curr_node = self.head.next
        l = []

        while curr_node != None:
            l.append(curr_node.value)
            curr_node = curr_node.next

        return l
        
