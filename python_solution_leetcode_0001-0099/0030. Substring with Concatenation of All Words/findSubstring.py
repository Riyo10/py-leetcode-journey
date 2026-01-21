from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_count = Counter(words)
        wlen = len(words[0])
        total = len(words)
        window = wlen * total
        n = len(s)

        res = []

        for offset in range(wlen):
            left = right = offset
            curr = Counter()

            while right + wlen <= n:
                word = s[right:right + wlen]
                right += wlen

                if word not in word_count:
                    curr.clear()
                    left = right
                    continue

                curr[word] += 1

                while curr[word] > word_count[word]:
                    lw = s[left:left + wlen]
                    curr[lw] -= 1
                    left += wlen

                if right - left == window:
                    res.append(left)

        return res
