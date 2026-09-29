
class ListNode:
    def __init__(self, val:int):
        self.val = val
        self.next= None


class MyLinkedList:
    def __init__(self): 
        self.head = ListNode(0)
        self.size = 0
        

    def get(self, index: int) -> int:
        print(self.size)
        if index >= self.size  :
            return -1 
        temp_head, start = self.head.next, 0 
        while start < index:
            start += 1
            temp_head = temp_head.next

        return temp_head.val

        

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size +=1
        

    def addAtTail(self, val: int) -> None:
        tail_node = ListNode(val)
        current_head = self.head
        while current_head.next:
            current_head = current_head.next
        current_head.next = tail_node
        self.size += 1

    
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        curr = self.head 
        
        start = 0
        while start < index:
            curr = curr.next
            start += 1
        
        new_node = ListNode(val)
        new_node.next = curr.next
        curr.next= new_node
        self.size += 1
 
    
        
    def deleteAtIndex(self, index: int) -> None:
        if self.size <= index:
            return     
        curr  = self.head
        start = 0 
        while start < index:
            start += 1
            curr = curr.next
        curr.next = curr.next.next
        self.size -=1


        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)