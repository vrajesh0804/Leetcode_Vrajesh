class Solution:
    def longestCommonPrefix(self, strs):
    	first, last = strs[0], strs[-1]
    	i = 0
    	while i < len(first) and i < len(last) and first[i] == last[i]:
    		i = i + 1
    	print(first[:i])


sol = Solution()
strs = ["aaa","aa","aaa"]
final = sol.longestCommonPrefix(strs)
