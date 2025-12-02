class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        ans = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x:
            d = x % 10
            x //= 10

            if ans > INT_MAX // 10 or (ans == INT_MAX // 10 and d > INT_MAX % 10):
                return 0

            ans = ans * 10 + d

        ans *= sign
        return ans if INT_MIN <= ans <= INT_MAX else 0
