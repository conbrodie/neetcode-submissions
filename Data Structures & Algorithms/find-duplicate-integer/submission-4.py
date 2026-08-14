class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # s = 2
        # f = 2
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        curr = 0
        while curr != slow:
            slow = nums[slow]
            curr = nums[curr]

        return curr
            

