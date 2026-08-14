class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = []
       
        for curr in range(len(temperatures)):
            fast = curr
            while fast < len(temperatures):
                if temperatures[fast] > temperatures[curr]:
                    ret.append(fast - curr)
                    break
                else:
                    fast += 1
            
            if fast >= len(temperatures):
                ret.append(0)

        return ret
