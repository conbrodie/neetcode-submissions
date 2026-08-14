class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for i in range(len(nums)):
            num_set.add(nums[i])
    
        return len(num_set) != len(nums)