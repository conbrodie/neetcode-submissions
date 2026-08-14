# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        leng = 0
        curr = head
        while curr:
            leng += 1
            curr = curr.next

        left_head = ListNode(0)
        left = left_head

        right_head = ListNode(0)
        right = right_head

        curr = head
        for _ in range(leng - (leng % k)):
            left.next = curr
            left = curr
            curr = curr.next

        right.next = left.next
        left.next = None

        prev_group = left_head
        curr = left_head.next

        while curr:
            group_start = curr
            prev = None
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            prev_group.next = prev
            prev_group = group_start

        prev_group.next = right.next
        return left_head.next
                