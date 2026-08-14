class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = []
        n = len(temperatures)
        for curr in range(n):
            fast = curr
            while fast < n:
                if temperatures[fast] > temperatures[curr]:
                    ret.append(fast - curr)
                    break
                else:
                    fast += 1
            
            if fast >= n:
                ret.append(0)

        return ret
