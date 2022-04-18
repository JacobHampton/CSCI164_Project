from time import time
from Algorithms import BFS, DFS, IDDFSOrig, RBFS, Astar
from Board import Board

state=[[1,6,0,2,7,3,4,8,5],
       [4,6,2,3,0,1,5,8,7],
       [8,2,1,5,7,4,3,6,0],
       [8,4,0,1,5,6,3,7,2],
       [5,3,0,4,7,8,1,2,6],
       [0,6,8,3,1,4,2,5,7],
       [4,5,3,2,0,7,1,8,6],
       [1,2,8,3,0,7,6,4,5],
       [0,3,5,6,8,4,7,1,2],
       [6,8,4,3,1,7,0,2,5],
       [0,2,8,5,1,4,6,3,7],
       [6,1,8,2,7,3,5,4,0],
       [0,4,2,3,8,5,6,7,1],
       [4,2,0,3,8,5,7,1,6],
       [0,5,4,6,7,2,8,1,3],
       [3,1,4,5,7,2,6,8,0],
       [6,3,7,2,1,8,0,4,5],
       [4,3,0,6,2,1,8,7,5],
       [1,5,8,2,7,4,0,3,6],
       [1,3,0,4,5,8,7,2,6],
       ]

for i in range(0,20):
    Board.nodes_expanded = 0
    Board.board_len = 3
    temp_start = [int(x) for x in state[i]]
    Board.start_state = temp_start
    Board.goal_state = [1,2,3,4,5,6,7,8,0]

    #Change Board.algorithm and heuristic_model if needed.

    Board.heuristic_model = "MD"
    Board.algorithm = "RBFS"

    print("Start State: ", Board.start_state)
    print("Goal State: ", Board.goal_state)

    t0 = time()
    print(Board.algorithm,": ", RBFS(Board.start_state))
    t1 = time() - t0
    
    print('Nodes Expanded:',Board.nodes_expanded)
    print('Time Spent: ', round(t1,3))
    print()
    print('------------------------------------------')
