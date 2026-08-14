class Solution:
    def isValid(self, s: str) -> bool:

        # ({})
        # ([{}]
        # stack is empty - add
        # stack[-1] == '(' and curr == ')' stack.pop

        stack = []
        top = ""
        for i in range(len(s)):
            
            if not stack:
                top = ""
            else:
                top = stack[-1]

            if s[i] == "}" and top != "{":
                return False
            elif s[i] == ")" and top != "(":
                return False
            elif s[i] == "]" and top != "[":
                return False
            elif s[i] == "[" or s[i] == "(" or s[i] == "{":
                stack.append(s[i])
            else: 
               stack.pop()

        return len(stack) == 0
        