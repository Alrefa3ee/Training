from pprint import pprint
import typing as t

n = 4
m = 8

arr = [[0 for j in range(m)] for i in range(n)]

# algorithm
def rays(arr: t.List[int], steps: int = 1, row: int = 0, col: int = 0, increasing_row: bool = True, increasing_col: bool = True):
    print(arr)
    if arr[-1][-1] != 0:
        return arr
    if row >= n-1: increasing_row = False
    elif row == 0: increasing_row = True
    if col >= m-1: increasing_col = False
    elif col == 0: increasing_col = True
        
    if arr[row][col] == 0:
        arr[row][col] = steps
    steps += 1
    row = row + 1 if increasing_row else row - 1
    col = col+1 if increasing_col else col-1
    return rays(arr, steps, row, col, increasing_row, increasing_col)


x= rays(arr)
pprint(x)
