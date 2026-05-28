class Puzzle:
    def __init__(self, state, parent=None, move="", depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth

    def get_blank(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def possible_moves(self):
        x, y = self.get_blank()
        moves = []

        directions = {
            "UP": (x-1, y),
            "DOWN": (x+1, y),
            "LEFT": (x, y-1),
            "RIGHT": (x, y+1)
        }

        for move, (i, j) in directions.items():
            if 0 <= i < 3 and 0 <= j < 3:
                new_state = [row[:] for row in self.state]
                new_state[x][y], new_state[i][j] = new_state[i][j], new_state[x][y]
                moves.append(Puzzle(new_state, self, move, self.depth+1))

        return moves