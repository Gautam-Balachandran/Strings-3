# Time Complexity : O(n)
# Space Complexity : O(1)
class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        cur, cal, tail = 0, 0, 0
        lastSign = '+'
        
        for i in range(len(s)):
            ch = s[i]
            if ch.isdigit():
                cur = cur * 10 + int(ch)
            if not ch.isdigit() and ch != ' ' or i == len(s) - 1:
                if lastSign == '+':
                    cal += cur
                    tail = cur
                elif lastSign == '-':
                    cal -= cur
                    tail = -cur
                elif lastSign == '*':
                    cal = cal - tail + tail * cur
                    tail *= cur
                elif lastSign == '/':
                    cal = cal - tail + int(tail / cur)
                    tail = int(tail / cur)
                
                lastSign = ch
                cur = 0
        
        return cal

# Examples
solution = Solution()

# Example 1
s1 = "3+2*2"
print("Expression: {}, Result: {}".format(s1, solution.calculate(s1))) # Output : 7

# Example 2
s2 = " 3/2 "
print("Expression: {}, Result: {}".format(s2, solution.calculate(s2))) # Output : 1

# Example 3
s3 = " 3+5 / 2 "
print("Expression: {}, Result: {}".format(s3, solution.calculate(s3))) # Output : 5