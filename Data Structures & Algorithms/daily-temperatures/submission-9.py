class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #                       |
        # [30, 38, 30, 36, 35, 40, 28]
        # [1,4,1,2,1,0,0]
        # [38,]
        output = [0] * len(temperatures) 
        stack = []
        for t in range(len(temperatures)):
            while stack and temperatures[t] > temperatures[stack[-1]]:
                output[stack[-1]] = t - stack[-1]
                stack.pop()
            
            stack.append(t)

        return output