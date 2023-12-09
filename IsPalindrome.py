# Leetcode #125

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for a in s:
            if a.isalpha() or a.isdigit():
                new += a.lower()
        return (new == new[::-1]) #new[::-1] reverses the string
    

test = Solution()
print(test.isPalindrome("A man, a plan, a canal: Panama")) #Should be true
print(test.isPalindrome("race a car")) #Should be fase
print(test.isPalindrome(" ")) #Should be true