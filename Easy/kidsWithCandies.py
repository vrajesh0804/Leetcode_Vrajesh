class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        final_out = []
        for candy in candies:
            maxi = max(candies)
            final_out_val = None
            new_candy_val = int(candy) + int(extraCandies)
            if new_candy_val >= maxi:
                final_out_val = True
                final_out.append(final_out_val)
            else:
                final_out_val = False
                final_out.append(final_out_val)
        return final_out

candies = [2,3,5,1,3]
extraCandies = 3
sol = Solution().kidsWithCandies(candies, extraCandies)
