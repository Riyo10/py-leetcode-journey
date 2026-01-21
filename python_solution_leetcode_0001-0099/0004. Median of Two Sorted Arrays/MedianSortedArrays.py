class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        def kth(i: int, j: int, k: int) -> int:
            if i == m:
                return nums2[j + k - 1]
            if j == n:
                return nums1[i + k - 1]
            if k == 1:
                return min(nums1[i], nums2[j])

            p = k // 2
            x = nums1[i + p - 1] if i + p - 1 < m else float("inf")
            y = nums2[j + p - 1] if j + p - 1 < n else float("inf")

            if x < y:
                return kth(i + p, j, k - p)
            else:
                return kth(i, j + p, k - p)

        total = m + n
        a = kth(0, 0, (total + 1) // 2)
        b = kth(0, 0, (total + 2) // 2)
        return (a + b) / 2
