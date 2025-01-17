# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Solution:
    def longestCommonPrefix(self, strs:list[str])->str:
        #Vertical search approach
        #Base Case
        if len(strs) == 0:
            return ""
        #Variables
        max_length = len(min(strs, key = len))
        
        #Nested loop
        for i in range(max_length):
            character =  strs[0][i]
            for string in strs:
                if string[i] != character:
                    return string[:i]
        
        return strs[0][:max_length]
        

        
        
solution= Solution()
strs = ["flower","flow","flight"]

solution.longestCommonPrefix(strs)