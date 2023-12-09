# Leetcode #1

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}  

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

test = Solution()
print(test.twoSum([2,7,11,15], 9)) #Should print [0,1]
print(test.twoSum([3,2,4], 6)) #Should print [1,2]
print(test.twoSum([3,3], 6)) #Should print [0,1]