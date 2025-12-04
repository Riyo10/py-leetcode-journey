class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0

        while l < r:
            h = height[l] if height[l] < height[r] else height[r]
            ans = max(ans, h * (r - l))
            l, r = (l + 1, r) if height[l] < height[r] else (l, r - 1)

        return ans
