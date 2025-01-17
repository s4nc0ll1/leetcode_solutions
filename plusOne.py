"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        #Variables
        i = len(digits) - 1

        #Loop where we simulate the sum process
        while i >= 0:
            digits[i] = digits[i] + 1
            if digits[i] >= 10:
                digits[i] = digits[i] - 10
                if i == 0:
                    digits.insert(0,1)
                    return digits
            else:
                return digits
            i -= 1