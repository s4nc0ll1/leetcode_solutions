class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
            i = 0
            j = 0

            while j < len(haystack):
                if haystack[j] == needle[i]:
                    i += 1
                    if i == len(needle):
                        return j - i + 1
                else:
                    j -= i
                    i = 0
                
                j += 1
                    
            return -1