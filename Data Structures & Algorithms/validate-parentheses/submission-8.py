class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ops = {')':'(','}':'{',']':'['}
        # ()
        for c in s:
            if c in ops:
                if stack and stack[-1] != ops[c]:
                    return False
                elif stack:
                    stack.pop()
                    continue

            stack.append(c)
        
        return len(stack) == 0