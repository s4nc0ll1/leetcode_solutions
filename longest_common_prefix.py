class Solution:
    def longestCommonPrefix(self, strs:List[str])->str:
        #Variables
        prefix = strs[0]
        #Base Case
        if strs == "":
            return ""
        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix =  prefix[:-1]
            if prefix == "":
                return prefix

        return prefix