class Solution:
	# Without using ListNode code
    def mergeTwoLists(self, list1, list2):
    	final_list = []
    	for i, j in zip(list1, list2):
    		final_list.append(i)
    		final_list.append(j)

    	return final_list

sol = Solution()
list1 = [1,2,4]
list2 = [1,3,4]
final = sol.mergeTwoLists(list1, list2)
print(final)