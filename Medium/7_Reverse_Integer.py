# LeetCode 7. Reverse Integer
# Difficulty: Medium

class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        reversed_num = 0

        while x_abs != 0:
            digit = x_abs % 10
            x_abs //= 10

            # Check for overflow before updating reversed_num
            if reversed_num > (INT_MAX - digit) // 10:
                return 0

            reversed_num = reversed_num * 10 + digit

        return sign * reversed_num
