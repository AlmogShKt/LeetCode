# 36
import collections


def isValidSudoku(self, board) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                board_value = board[r][c]
                if board_value == ".":
                    continue
                if (board_value in rows[r] or
                        board_value in cols[c] or
                        board_value in squares[(r // 3, c // 3)]):
                    return False
                rows[r].add(board_value)
                cols[c].add(board_value)
                squares[(r // 3, c // 3)].add(board_value)
        return True

