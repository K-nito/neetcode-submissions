class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Matches = { ")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c not in Matches:
                stack.append(c)
            else:
                if stack and stack[-1] == Matches[c]:
                    stack.pop()
                else:
                    return False

        return not stack