class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        i, n = 0, len(s)
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0

        sign = 1
        if s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1

        res = 0
        limit = INT_MAX // 10  

        while i < n and s[i].isdigit():
            d = ord(s[i]) - 48

            if res > limit or (res == limit and d > 7):
                return INT_MAX if sign == 1 else INT_MIN

            res = res * 10 + d
            i += 1

        return sign * res
