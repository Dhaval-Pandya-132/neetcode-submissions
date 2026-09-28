# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        output = result

        if not list1:
            return list2
        
        if not list2:
            return list1

        while list1 and list2:
            if list1.val >= list2.val:
                result.next = ListNode(list2.val)
                list2 = list2.next
            else :
                result.next = ListNode(list1.val)
                list1 = list1.next
                
            result = result.next
        
        while list1:
            result.next = ListNode(list1.val)
            list1 = list1.next
            result = result.next

        while list2:
            result.next = ListNode(list2.val)
            list2 = list2.next
            result = result.next

        
        return output.next


