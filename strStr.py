class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
            i = 0
            j = 0

            while j < len(haystack):
                if haystack[j] == needle[i]:
                    #print(f"Match: {haystack[j]} , {needle[i]}")
                    i += 1
                    if i == len(needle):
                        return j - i + 1
                else:
                    #print(f"Mismatch: { haystack[j]} , {needle[i]}")
                    j -= i
                    i = 0
                
                j += 1
                    
            return -1