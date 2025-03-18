class Solution:
    def twoSum(self, nums, target):
        for val1 in range(len(nums)):
            for val2 in range(val1 + 1, len(nums)):
                sum_two = nums[val1] + nums[val2]
                if target == sum_two:
                    print(f'[{val1},{val2}]')
                    return

# Example usage
nums = [2, 7, 11, 15]
target = 9

sol = Solution()
sol.twoSum(nums, target)
