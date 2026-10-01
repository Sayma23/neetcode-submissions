class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        blocks = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if(board[r][c] != "."):
                    cur = board[r][c]
                    if(cur in rows[r] or cur in cols[c]  or cur in blocks [(r//3) * 3 + c//3]):
                        return False
                    rows[r].add(cur)
                    cols[c].add(cur)
                    blocks [(r//3) * 3 + c//3].add(cur)
        return True
