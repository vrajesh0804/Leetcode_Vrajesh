class Solution:
    def removeElement(self, nums, val):
    	final_output = []
    	for num in nums:
    		if num != val:
    			final_output.append(num)

    	return final_output


nums = nums = [0,1,2,2,3,0,4,2]
val = 2
sol = Solution()
length = sol.removeElement(nums, val)
print(length)