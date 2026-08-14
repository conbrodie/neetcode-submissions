class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nmap:
                return [min(i, nmap[diff]), max(i, nmap[diff])]

            nmap[nums[i]] = i
        
