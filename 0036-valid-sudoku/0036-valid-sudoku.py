class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #create hash set
        checking_set = set()
        #check for rows
        for row in board:
            for value in row:
                if value not in checking_set:
                    checking_set.add(value)
                elif value == ".":
                    pass
                elif value in checking_set:
                    return False
            checking_set.clear()
        #check for columns
        for i in range(0,len(board[0])):
            for j in range(0,len(board)):
                if board[j][i] not in checking_set:
                    checking_set.add(board[j][i])
                elif board[j][i] == ".":
                    pass
                elif board[j][i] in checking_set:
                    return False
            checking_set.clear()
        # now valid square
        #traverse left to right and then top to down
        for r in range(0,9,3):
            for c in range(0,9,3):
                box_set = set()
                for i in range(3):
                    for j in range(3):
                        val = board[r+i][c+j]
                        if val in box_set:
                            return False
                        elif val == ".":
                            pass
                        else:
                            box_set.add(val)
        return True