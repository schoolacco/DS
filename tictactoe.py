import numpy as np
i = 0
board = np.array([["X"," ","0"],
         ["0","X"," "],
         ["X"," ","0"]])
for item in board:
    for item in board[i]:
        print(item, end=" ")
    if i < 2:
      i += 1
    print()