class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        half_reverse = 0
        
        while half_reverse < x:
            half_reverse = half_reverse * 10 + (x % 10)
            x //= 10

        return half_reverse == x or half_reverse // 10 == x