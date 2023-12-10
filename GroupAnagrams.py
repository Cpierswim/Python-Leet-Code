import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = collections.defaultdict(list)


        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
    

test = Solution()  
    
strs = ["eat","tea","tan","ate","nat","bat"]
print(test.groupAnagrams(strs)) #Should be [["bat"],["nat","tan"],["ate","eat","tea"]]

strs = [""]
print(test.groupAnagrams(strs)) #Should be [[""]]

strs = ["a"]
print(test.groupAnagrams(strs)) #Should be [["a"]]

