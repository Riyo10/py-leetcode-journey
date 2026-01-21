class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(start, rem, path):
            if rem == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > rem:
                    break
                dfs(i + 1, rem - candidates[i], path + [candidates[i]])

        dfs(0, target, [])
        return res
