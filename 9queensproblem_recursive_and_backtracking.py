def solve(col,queens):
    if col == 9:
        print("solution:",queens)
        return
    for row in range(9):
        if is_safe(row,col,queens):
            queens[col]=row
            solve(col+1,queens)
            queens[col]=-1
