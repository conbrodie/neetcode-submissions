class Solution:
    def isValid(self, s: str) -> bool:

        # ({})
        # (}
        # stack is empty - add
        # stack[-1] == '(' and curr == ')' stack.pop

        stack = []
        pairs = { ']': '[', '}': '{', ')':'(' }

        for c in s:
            if c in pairs:
                if stack and pairs[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
        