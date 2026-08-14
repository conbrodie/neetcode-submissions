# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        curr = slow
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        left = head
        right = prev
        while left and left.next and right and right.next:
            rightNxt = right.next 
            leftNxt = left.next

            left.next = right 
            right.next = leftNxt

            left = leftNxt
            right = rightNxt

        