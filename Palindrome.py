class Solution:
    def isPalindrome(self, int_number: int) -> bool:
        if int_number < 0 or (int_number % 10 == 0 and int_number != 0):
            return False

        rev_half = 0
        while int_number > rev_half:
            rev_half = rev_half * 10 + int_number % 10
            int_number //= 10
        
        return int_number == rev_half or int_number == rev_half // 10

