class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        best = (0, 0)
        for i in range(n):
            for a, b in (expand(i, i), expand(i, i + 1)):
                if b - a > best[1] - best[0]:
                    best = (a, b)

        return s[best[0]:best[1] + 1]
