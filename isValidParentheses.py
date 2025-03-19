class Solution:
	def isValid(self, s: str) -> bool:
		container = []
		parenthesisParing = {')': '(', '}': '{', ']': '['}
		for char in s:
			if char in parenthesisParing:
				top_element = container.pop() if container else '#'
				if parenthesisParing[char] != top_element:
					return False
			else:
				container.append(char)
		return not container 


sol = Solution()
string = "()][]"
final = sol.isValid(string)
print(final)