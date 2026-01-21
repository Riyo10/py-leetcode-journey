class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]
        empty = []

        # Initialize tracking arrays
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    num = int(board[r][c]) - 1
                    rows[r][num] = True
                    cols[c][num] = True
                    boxes[(r // 3) * 3 + (c // 3)][num] = True

        def backtrack(idx: int) -> bool:
            if idx == len(empty):
                return True

            r, c = empty[idx]
            box = (r // 3) * 3 + (c // 3)

            for num in range(9):
                if not rows[r][num] and not cols[c][num] and not boxes[box][num]:
                    board[r][c] = str(num + 1)
                    rows[r][num] = cols[c][num] = boxes[box][num] = True

                    if backtrack(idx + 1):
                        return True

                    board[r][c] = "."
                    rows[r][num] = cols[c][num] = boxes[box][num] = False

            return False

        backtrack(0)
