# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self , val= 0):
        self.val = val 
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.dummy = Node()

    def get(self, index: int) -> int:
        head = self.dummy.next
        temp = head
        count = 0 

        while temp and count < index:
            temp = temp.next
            count += 1
        
        if count == index and temp:
            return temp.val

        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.dummy.next
        self.dummy.next = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        temp = self.dummy

        while temp and temp.next :
            temp = temp.next
        temp.next = new_node


    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val) 
        
        temp = self.dummy
        count = 0 
        while temp.next and count < index:
            temp = temp.next
            count += 1
        
        if count != index:
            return
        
        new_node.next = temp.next
        temp.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        prev = self.dummy
        count = 0

        while prev.next  and count < index :
            prev = prev.next
            count += 1

        if count != index:
            return 

        if prev.next is None:
            return

        prev.next = prev.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)