class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I':1, 'V':5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        n = len(s)
        for i in range(n):
            if i < (n-1) and values[s[i]] < values[s[i+1]]:
                result -= values[s[i]]
            else:
                result += values[s[i]] 
       
        return result
                