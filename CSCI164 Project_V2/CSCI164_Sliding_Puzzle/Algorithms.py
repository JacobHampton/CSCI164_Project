from queue import Queue
from queue import PriorityQueue
from queue import LifoQueue
from Board import Board
from sys import maxsize

#BFS--------------------------------------
def BFS(initial_state):
    start_node = Board(initial_state, None, None, 0, 0)
    if start_node.state == Board.goal_state:
        return start_node.find_solution()
    frontier = Queue()
    frontier.put(start_node)
    explored=[]
    while not(frontier.empty()):
        if Board.nodes_expanded >= 50000:
            return "Nodes Expanded Limit Exceeded"
        node=frontier.get()
        explored.append(node.state)
        children=node.expand()
        for child in children:
            if child.state not in explored:
                if child.state == Board.goal_state:
                    return child.find_solution()
                frontier.put(child)
    return

#DFS--------------------------------------
def DFS(initial_state):
    start_node = Board(initial_state, None, None, 0, 0)
    if start_node.state == Board.goal_state:
        return start_node.find_solution()
    frontier = LifoQueue()
    frontier.put(start_node)
    explored=[]
    while not frontier.empty():
        if Board.nodes_expanded >= 50000:
            return "Nodes Expanded Limit Exceeded"
        node=frontier.get()
        explored.append(node.state)
        children=node.expand()
        for child in children:
            if child.state not in explored:
                if child.state == Board.goal_state:
                    return child.find_solution()
                frontier.put(child)
    return

#IDDFS--------------------------------------
def IDDFSOrig(initial_state):
    start_node = Board(initial_state, None, None, 0, False, 0)

    for depth in range(maxsize):
        found, remaining = DLSorig(start_node, depth)
        if found != None:
            return found.find_solution()
        elif not remaining:
            return None

def DLSorig(node, depth):
    #Early termination using nodes_expanded
    if Board.nodes_expanded >= 5000000:
        any_remaining = 0
        return (None, any_remaining)

    if depth == 0:
        if node.state == Board.goal_state:
            return (node, True)
        else:
            return(None, True)
    elif depth > 0:
        any_remaining = False
        children=node.expand()
        for child in children:
            found, remaining = DLSorig(child, depth-1)
            if found != None:
                return(found, True)
            if remaining:
                any_remaining = True
        return (None, any_remaining)


#A*----------------------------------------
def Astar(initial_state):
    count=0
    explored=[]
    start_node=Board(initial_state,None,None,0,0,True)
    frontier = PriorityQueue()
    frontier.put((start_node.evaluation_function,count,start_node))

    while not frontier.empty():
        if Board.nodes_expanded >= 50000:
            return "Nodes Expanded Limit Exceeded"
        node=frontier.get()
        node=node[2]
        explored.append(node.state)
        if node.state == Board.goal_state:
            return node.find_solution()

        children=node.expand()
        for child in children:
            if child.state not in explored:
                count += 1
                frontier.put((child.evaluation_function,count,child))
    return

#RBFS (Recursive A*)-----------------------------
def RBFS(initial_state):
    node=RBFS_search(Board(initial_state, None, None, 0, 0, True), f_limit=maxsize)
    node=node[0]
    if node == 0:
        return "Nodes Expanded Limit Exceeded"
    else:
        return node.find_solution()

def RBFS_search(node, f_limit):
    successors=[]
    if node.state == node.goal_state:
        return node,None
    children=node.expand()
    if not len(children):
        return None, maxsize
    count=-1
    for child in children:
        count+=1
        successors.append((child.evaluation_function,count,child))
    while len(successors):
        successors.sort()
        best_node=successors[0][2]
        if best_node.evaluation_function > f_limit:
            return None, best_node.evaluation_function
        alternative=successors[1][0]
        result,best_node.evaluation_function=RBFS_search(best_node, min(f_limit,alternative))
        successors[0]=(best_node.evaluation_function,successors[0][1],best_node)
        if Board.nodes_expanded >= 2000000:
            return 0, None
        if result!=None:
            break
    return result,None
