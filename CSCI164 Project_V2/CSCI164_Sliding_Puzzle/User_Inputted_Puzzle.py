import argparse
from Algorithms import BFS, DFS, IDDFSOrig, RBFS, Astar
from time import time
from Board import Board

#VSCODE sample argument structure
#"args":["--algorithm", "RBFS*MD", "--board_size", "15", "--start_state", "7DB13C52F46E80A9", "--goal_state", "123456789ABCDEF0", "--solution_string", "ULR"],
#"args":["--algorithm", "RBFS*MD", "--board_size", "8", "--start_state", "123456780", "--goal_state", "123456780", "--solution_string", "ULR"],

parser = argparse.ArgumentParser()
parser.add_argument('--algorithm', type=str, required=False, help='BFS, DFS, IDDFS, A*MD, RBFS*MD, A*OOP, RBFS*OOP')
parser.add_argument('--board_size', type=int, required=False, help='Number of squares (8 or 15)')
parser.add_argument('--start_state', required=False, type=str, help="Use format 123456780 or 123456789ABCDEF0")
parser.add_argument('--goal_state', required=False, type=str, help="Use format 123456780 or 123456789ABCDEF0")
parser.add_argument('--solution_string', required=False, type=str, help="Use format UDLR")
args = parser.parse_args()

if args.board_size == 8:
    Board.board_len = 3
elif args.board_size == 15:
    Board.board_len = 4
    
temp_start = [str(x) for x in args.start_state]
temp_goal = [str(x) for x in args.goal_state]



#If 15 puzzle, converts the letters to a numerical value (10-15)
if Board.board_len == 4:
    for num in range (0, 16):
        temp2 = temp_start[num]
        if temp_start[num] == 'A' or temp_start[num] == 'B' or temp_start[num] == 'C' or temp_start[num] == 'D' or temp_start[num] == 'E' or temp_start[num] == 'F':
            temp_start[num] = ord(temp_start[num]) - 55 
        if temp_goal[num] == 'A' or temp_goal[num] == 'B' or temp_goal[num] == 'C' or temp_goal[num] == 'D' or temp_goal[num] == 'E' or temp_goal[num] == 'F':
            temp_goal[num] = ord(temp_goal[num]) - 55 

start_state_arg = [int(x) for x in temp_start]
goal_state_arg = [int(x) for x in temp_goal]

#Board size argument checker
if args.board_size == 8:
    if len(start_state_arg) != 9:
        raise ValueError("Start_state length is not valid")
    elif len(goal_state_arg) != 9:
        raise ValueError("Goal_state length is not valid")
elif args.board_size == 15:
    if len(start_state_arg) != 16:
        raise ValueError("Start_state length is not valid")
    elif len(goal_state_arg) != 16:
        raise ValueError("Goal_state length is not valid")
else:
    raise ValueError("Puzzle Length is not valid")


Board.start_state = start_state_arg
Board.goal_state = goal_state_arg


if args.solution_string != None: 
    solution_string = args.solution_string
    print("Trying test solution moves..")
    print("Starting state: ", Board.start_state)
    print("After moves state: ", Board.test_solution(solution_string))
    print()


if args.algorithm != None:
    print("Start State: ", Board.start_state)
    print("Goal State: ", Board.goal_state)

    Board.algorithm = args.algorithm

    if args.algorithm == "BFS":
        t0 = time()
        print('BFS:', BFS(Board.start_state))
        t1 = time() - t0
        print('Nodes Expanded:',Board.nodes_expanded)
        print('Time Spent: ', round(t1,3))
        print()

    elif args.algorithm == "DFS":
        t0 = time()
        print('DFS:', DFS(Board.start_state))
        t1 = time() - t0
        print('Nodes Expanded:',Board.nodes_expanded)
        print('Time Spent: ', round(t1,3))
        print()

    elif args.algorithm == "A*OOP":
        Board.heuristic_model = "OOP"
        t0 = time()
        print('A* with Out of Place:', Astar(Board.start_state))
        t1 = time() - t0
        print('Nodes Expanded:',Board.nodes_expanded)
        print('Time Spent: ', round(t1,3))
        print()

    elif args.algorithm == "A*MD":
        Board.heuristic_model = "MD"
        t0 = time()
        print('A* with Manhattan Distance:', Astar(Board.start_state))
        t1 = time() - t0
        print('Nodes Expanded:',Board.nodes_expanded)
        print('Time Spent: ', round(t1,3))
        print()

    elif args.algorithm == "IDDFS":
        t0 = time()
        print('IDDFS:', IDDFSOrig(Board.start_state))
        t1 = time() - t0
        print('Nodes Expanded:',Board.nodes_expanded)
        print('Time Spent: ', round(t1,3))
        print()

    elif args.algorithm == "RBFS*OOP":
       
        Board.heuristic_model = "OOP"
        t0 = time()
        print('RBFS with Out of Place:', RBFS(Board.start_state))
        t1 = time() - t0
        print('Nodes Expanded:',Board.nodes_expanded)
        print('Time Spent: ', round(t1,3))
        print()

    elif args.algorithm == "RBFS*MD":
        
        Board.heuristic_model = "MD"
        t0 = time()
        print('RBFS with Manhattan Distance:', RBFS(Board.start_state))
        t1 = time() - t0
        print('Nodes Expanded:',Board.nodes_expanded)
        print('Time Spent: ', round(t1,3))
        print()


