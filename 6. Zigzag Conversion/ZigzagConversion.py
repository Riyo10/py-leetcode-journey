class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        idx, dir = 0, 1

        for c in s:
            rows[idx] += c
            if idx == 0: dir = 1
            elif idx == numRows - 1: dir = -1
            idx += dir

        return ''.join(rows)
