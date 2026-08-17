class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1
        while l < r:
            mid = (l+r) //2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        part = l

        def bs(l: int, r: int) -> int:
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return -1

        arr_1_res = bs(0, part - 1)
        if arr_1_res != -1:
            return arr_1_res
        
        return bs(part, len(nums) - 1)