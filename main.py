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
        if row[box_col_idx] == value:
            return False
    return True

def grid_check(board, box_row_idx, box_col_idx, value):
    # get location of the box: 
    # 1) Left, middle or top column of the three
    # 2) Upper, middle or Lower row of the three
    
    col_start, col_end = 0, 0
    row_start, row_end = 0, 0
    
    # Task 1:
    if box_col_idx % 3 == 0:
        col_start, col_end = box_col_idx, box_col_idx + 2
    elif (box_col_idx + 1) % 3 == 0:
        col_start, col_end = box_col_idx - 2, box_col_idx
    else:
        col_start, col_end = box_col_idx - 1, box_col_idx + 1
    
    # Task 2:
    if box_row_idx % 3 == 0:
        row_start, row_end = box_row_idx, box_row_idx + 2
    elif (box_row_idx + 1) % 3 == 0:
        row_start, row_end = box_row_idx - 2, box_row_idx
    else:
        row_start, row_end = box_row_idx - 1, box_row_idx + 1
        
    for row in range(row_start, row_end + 1):
        for col in range(col_start, col_end + 1):
            if board[row][col] == value:
                return False
    return True

def is_valid_move(board, box_row_idx, box_col_idx, value):
    if row_check(board, box_row_idx, value) and col_check(board, box_col_idx, value) and grid_check(board, box_row_idx, box_col_idx, value):
        return True
    else:
        return False

def solve(board):
    pass