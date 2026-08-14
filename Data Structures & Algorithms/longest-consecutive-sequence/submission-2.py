class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort nums asc
        nums = sorted(nums)
        groups = 0;
        sequences = {}
        # groupNum = 0
        # sort asc -> iterate -> check currVal - 1 == i - 1 -> add(0, currVal)
        # if not groupNum++ -> check currVal - 1 == i - 1 -> add(1, currVal)
        if (len(nums)) == 0:
            return 0;
        for i in range(len(nums)):
            currentVal = nums[i]
            if i == 0:
                sequences[0] = [nums[i]]
                continue
            if currentVal == nums[i - 1]:
                continue
            if currentVal - 1 == nums[i - 1]:
                sequences[groups].append(nums[i])
            else:
                groups += 1
                sequences[groups] = [nums[i]]

        return len(sequences[max(sequences, key=lambda k: len(sequences[k]))])





