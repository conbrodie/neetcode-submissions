class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        n = len(temperatures)
        for currTemp in range(n):
            futureTemp = currTemp+1
            while futureTemp < n:
                if temperatures[futureTemp] > temperatures[currTemp]:
                    output.append(futureTemp - currTemp)
                    break
                else:
                    futureTemp += 1
            
            if futureTemp >= n:
                output.append(0)

        return output
