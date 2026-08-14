class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = {}
        for i in range(len(nums)):
            num_to_find = target - nums[i]
            if num_to_find in nmap:
                return [min(i, nmap[num_to_find]), max(i, nmap[num_to_find])]
                
            nmap[nums[i]] = i
        
