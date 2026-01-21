class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(start, remain, path):
            if remain == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break
                dfs(i, remain - candidates[i], path + [candidates[i]])

        dfs(0, target, [])
        return res
