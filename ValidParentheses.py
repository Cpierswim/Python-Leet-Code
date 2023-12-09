# Leetcode #20

class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
    
test = Solution()

print(test.isValid("()")) #Should be true
print(test.isValid("(]")) #Should be false
print(test.isValid("()[]{}")) #Should be true