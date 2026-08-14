# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head == None:
            return head

        length = 0
        curr = head
        while curr:
            length += 1 
            curr = curr.next

        dummy = ListNode()
        node = dummy
        curr = head
        target = length - n
        i = 0
        while curr:
            if i != target:
                node.next = curr
                node = curr
                
            i += 1
            curr = curr.next

        node.next = None
        return dummy.next

          




# 1 2 3 4
# 