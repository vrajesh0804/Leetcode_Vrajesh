class Solution:
	def removeDuplicates(self, nums):
		unique_index = 0
		for i in range(1, len(nums)):
			if nums[i] != nums[unique_index]:
				unique_index += 1
				nums[unique_index] = nums[i]  
		return unique_index + 1

nums = [0, 9, 1, 1, 2, 2, 3, 3, 9]
sol = Solution()
length = sol.removeDuplicates(nums)
print(nums[:length])
