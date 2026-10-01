class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        blocks = [0] * 9
        for i in range(9):
            for j in range(9):
                if(board[i][j] != "."):
                    cur = int(board[i][j])- 1
                    if (rows[i] & (1 << cur) or cols[j] & (1 << cur) or blocks[(i//3) * 3 + (j //3)] & (1 << cur)):
                        return False
                    
                    rows[i] |= (1 << cur)
                    cols[j] |= (1 << cur)
                    blocks[(i//3) * 3 + (j //3)] |= (1 << cur)
        return True
