"""
Given two binary strings a and b, return their sum as a binary string.
Example 1:
Input: a = "11", b = "1"
Output: "100"
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #Variables
        a_int = int(a, 2)
        b_int = int(b, 2)
        #Sum and format back to binary
        result = a_int + b_int
        result_bin = format(result, 'b')
        return result_bin