class Board:
    board_len = None
    algorithm = None
    goal_state = None 
    start_state = None
    heuristic = None
    heuristic_model = None
    evaluation_function= None
    needs_hueristic = False
    nodes_expanded = 0
    def __init__(self,state,parent,action,path_cost, depth, needs_hueristic = False):
        self.parent = parent
        self.state = state
        self.action = action
        self.depth = depth
        if parent:
            self.path_cost = parent.path_cost + path_cost
        else:
            self.path_cost = path_cost
        if self.algorithm == "BFS" or self.algorithm == "DFS" or self.algorithm == "IDDFS":
            needs_hueristic = False
        else:
            needs_hueristic = True

        if needs_hueristic:
            self.needs_hueristic = True
            if self.heuristic_model == "MD":
                self.Manhattan_Distance()
            elif self.heuristic_model == "OOP":
                self.Out_of_Place()
            else: 
                raise ValueError("Not a valid heuristic, try MD or OOP")
            
            self.evaluation_function = self.heuristic + self.path_cost

    def Manhattan_Distance(self):
        self.heuristic = 0
        for num in range(1,self.board_len*self.board_len):
            distance=abs(self.state.index(num) - self.goal_state.index(num))
            i=int(distance / self.board_len)
            j=int(distance % self.board_len)
            self.heuristic = self.heuristic+i+j
    
    def Out_of_Place(self):
        self.heuristic = 0
        for num in range(1,self.board_len*self.board_len):
            if self.state.index(num) != Board.goal_state.index(num):
                self.heuristic += 1
            elif self.state.index(num) == Board.goal_state.index(num):
                self.heuristic -= 1
            
    @staticmethod
    def moves(i,j):
        moves = ['U', 'D', 'L', 'R']
        if i == 0:  
            moves.remove('U')
        elif i == Board.board_len - 1:  
            moves.remove('D')
        if j == 0:
            moves.remove('L')
        elif j == Board.board_len - 1:
            moves.remove('R')
        return moves

    def expand(self):
        children=[]
        x = self.state.index(0)
        i = int(x / Board.board_len)
        j = int(x % Board.board_len)
        moves = self.moves(i,j)

        Board.nodes_expanded += 1
        for move in moves:
            new_state = self.state.copy()
            if move == 'U':
                new_state[x], new_state[x-Board.board_len] = new_state[x-Board.board_len], new_state[x]
            elif move == 'D':
                new_state[x], new_state[x+Board.board_len] = new_state[x+Board.board_len], new_state[x]
            elif move == 'L':
                new_state[x], new_state[x-1] = new_state[x-1], new_state[x]
            elif move == 'R':
                new_state[x], new_state[x+1] = new_state[x+1], new_state[x]
            children.append(Board(new_state,self,move,1,self.needs_hueristic))
        return children

    def find_solution(self):
        solution = []
        solution.append(self.action)
        path = self
        while path.parent != None:
            path = path.parent
            solution.append(path.action)
        solution = solution[:-1]
        solution.reverse()
        return solution

    def test_solution(move_list):
        move = [str(x) for x in move_list]
        new_state = Board.start_state

        for num in range(0, len(move_list)):
            x = new_state.index(0)
            i = int(x / Board.board_len)
            j = int(x % Board.board_len)
            if move[num] == 'U':
                if i != 0:
                    new_state[x], new_state[x-Board.board_len] = new_state[x-Board.board_len], new_state[x]
            elif move[num] == 'D':
                if i != Board.board_len - 1:
                    new_state[x], new_state[x+Board.board_len] = new_state[x+Board.board_len], new_state[x]
            elif move[num] == 'L':
                if j != 0:
                    new_state[x], new_state[x-1] = new_state[x-1], new_state[x]
            elif move[num] == 'R':
                if j == Board.board_len - 1:    
                    new_state[x], new_state[x+1] = new_state[x+1], new_state[x]    
        return new_state    

