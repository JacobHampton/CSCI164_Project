from time import time
from Algorithms import BFS, DFS, IDDFSOrig, RBFS, Astar
from Board import Board

goal_state = [1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F',0]

state = [[1,6,2,3,5,'A',7,4,9,'C',0,8,'D','E','B','F'],
          [0,6,3,4,2,1,7,8,5,9,'A','B','D','E','F','C'],
          [0,1,2,4,5,6,3,7,9,'B','C',8,'D','A','E','F'],
          [5,1,2,4,6,'A',3,8,0,9,7,'B','D','E','F','C'],
          [1,2,3,4,5,6,7,8,'D',9,'C','F','E','B','A',0],
          [7,1,'A',9,2,'C','E',0,3,'D','B',4,6,5,8,'F'],
          [0,2,3,4,8,6,9,7,'D','F',5,'A',1,'E','B','C'],
          [3,9,'A',1,'D',0,'E','C',7,'B','F',8,6,4,5,2],
          ['E','A','B',4,8,0,'F','C',1,9,'D',5,6,2,3,7],
          [7,'D','B',1,3,'C',5,2,'F',4,6,'E',8,0,'A',9],
        ]

#Gets goal and converts to int list
temp_goal = [str(x) for x in goal_state]
for num in range(0, 16):
    if temp_goal[num] == 'A' or temp_goal[num] == 'B' or temp_goal[num] == 'C' or temp_goal[num] == 'D' or temp_goal[num] == 'E' or temp_goal[num] == 'F':
        temp_goal[num] = ord(temp_goal[num]) - 55
converted_goal = [int(x) for x in temp_goal]



for i in range(0,10):
    temp_start = [str(x) for x in state[i]]

    for num in range (0, 16):
        if temp_start[num] == 'A' or temp_start[num] == 'B' or temp_start[num] == 'C' or temp_start[num] == 'D' or temp_start[num] == 'E' or temp_start[num] == 'F':
            temp_start[num] = ord(temp_start[num]) - 55 
    converted_start = [int(x) for x in temp_start]
    
    Board.nodes_expanded = 0
    Board.board_len = 4
    Board.goal_state = converted_goal
    Board.start_state = converted_start

    #Change Board.algorithm and heuristic_model if needed.

    #Board.heuristic_model = "OOP"
    Board.algorithm = "IDDFS"

    print("Start State: ", state[i])
    print("Goal State: ", goal_state)

    t0 = time()
    print(Board.algorithm, ': ', IDDFSOrig(Board.start_state))
    t1 = time() - t0
    print('Nodes Expanded:',Board.nodes_expanded)
    print('Time Spent: ', round(t1,3))
    print()
    print('------------------------------------------')
