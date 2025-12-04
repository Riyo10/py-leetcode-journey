class Solution:
    def intToRoman(self, num: int) -> str:
        cs = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        vs = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)

        ans = []
        for c, v in zip(cs, vs):
            count, num = divmod(num, v)
            ans.append(c * count)

        return ''.join(ans)
