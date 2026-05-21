class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = {}
        col_dict = {}
        square_dict = {}

        for row, alos in enumerate(board):
            row_dict[row] = set()
            for col, s in enumerate(alos):
                if s != ".":
                    val = int(s)
                    square = (row // 3) * 3 + (col // 3)
                    if col not in col_dict:
                        col_dict[col] = set()
                    if square not in square_dict:
                        square_dict[square] = set()

                    if val in row_dict[row] or val in col_dict[col] or val in square_dict[square]:
                        return False
                    
                    row_dict[row].add(val)
                    col_dict[col].add(val)
                    square_dict[square].add(val)
        
        return True

