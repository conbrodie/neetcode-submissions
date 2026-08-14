class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4,-1,-1,0,1,2]
        # -1 -1 2
        nums.sort()
        output = []
        for center in range(len(nums)):
        
            # once we validate all possible triplets for a center
            # if the previous center is the same as the new center skip forward as we have gotten all possible triplets below
            if center > 0 and nums[center] == nums[center-1]:
                continue

            l = center + 1
            r = len(nums) - 1
            while l < r:
                total_sum = nums[center] + nums[l] + nums[r]
                if total_sum == 0:
                    output.append([nums[center], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        # keep checking for valid triplets for the center number
                        # [-1,-1,2] has been found but [-1,1,0] is yet to be found for the current center - we need to keep checking
                        l +=1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif total_sum < 0:
                    l += 1
                else:
                    r -= 1

        return output
        

