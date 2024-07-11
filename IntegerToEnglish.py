# Time Complexity : O(1), as the number of digits in an integer is limited, and
# the operations performed are independent of the number size.
# Space Complexity : O(1), as the space used does not grow with the size of the
# input number.  It is limited by the recursive calls and the storage of
# intermediate strings, which is bounded by the maximum number of digits in an
# integer.
class Solution:
    LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
                    "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                    "Eighteen", "Nineteen"]
    TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy",
            "Eighty", "Ninety"]
    THOUSANDS = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        return self.convertToString(num).strip()
    
    def convertToString(self, num: int) -> str:
        if num == 0:
            return ""
        elif num < 20:
            return self.LESS_THAN_20[num] + " "
        elif num < 100:
            return self.TENS[num // 10] + " " + self.convertToString(num % 10)
        elif num < 1000:
            return self.LESS_THAN_20[num // 100] + " Hundred " + self.convertToString(num % 100)
        else:
            for i in range(3, 0, -1):
                divisor = 1000 ** i
                if num >= divisor:
                    return self.convertToString(num // divisor) + self.THOUSANDS[i] + " " + self.convertToString(num % divisor)
        return ""

# Examples
solution = Solution()

# Example 1
num1 = 123
print("Number: {}, Words: {}".format(num1, solution.numberToWords(num1))) # Output : One Hundred Twenty Three

# Example 2
num2 = 12345
print("Number: {}, Words: {}".format(num2, solution.numberToWords(num2))) # Output : Twelve Thousand Three Hundred Forty Five

# Example 3
num3 = 1234567
print("Number: {}, Words: {}".format(num3, solution.numberToWords(num3)))