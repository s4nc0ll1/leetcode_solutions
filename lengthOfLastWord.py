"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strings = s.strip().split(" ")
        """
        for string in strings:
            if string == '':
                strings.remove('')
        print(strings)
        """
        
        return len(strings[-1])


test = "  fly me   to   the moon  "
result =  Solution()
print(result.lengthOfLastWord(test))