board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):
    for row_idx, row in enumerate(board):
        print("--------------------------")
        for col_idx, col in enumerate(row):
            print(col, end=" ")
            if col_idx == 8:
                print("||")
            elif (col_idx + 1) % 3 == 0 and col_idx != 0:
                print("||", end=" ")
    print("--------------------------")
    
def row_check(board, box_row_idx, value):
    row = board[box_row_idx]
    
    for row_val in row:
        if row_val == value:
            return False
    return True    
        
def col_check(board, box_col_idx, value):
    for row in board:
        print(row[box_col_idx])
        if row[box_col_idx] == value:
            return False
    return True

def grid_check(board):
    pass

def solve(board):
    pass

# Run tests:
# print_board(board)
# print(row_check(board, 1, 8))
# print(col_check(board, 8, 6))