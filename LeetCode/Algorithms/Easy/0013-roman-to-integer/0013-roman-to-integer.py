class Solution:
    def romanToInt(self, s: str) -> int:
        change_to_int = { 'I':1, 'V':5, "X":10, 'L':50, 'C':100, 'D':500, 'M':1000  }
        
        result = 0

        for i in range(len(s)):
            if i + 1 < len(s) and change_to_int[s[i]] < change_to_int[s[i+1]]:
                result -= change_to_int[s[i]]
            else:
                result += change_to_int[s[i]]
        return result