from games import *
from copy import deepcopy

class Notakto(Game):
    def __init__(self, board):
        self.board_size = len(board)
        self.value = len(board)**2
        self.initial = GameState(to_move='Max', utility=0, board=board, moves=self.getmoves(board))


    # returns a list of legal moves given a state
    def actions(self, state):
        return state.moves.copy()

    # returns a list of the legal moves given a board
    def getmoves(self, board):
        moves = []

        def is_inbound(x, y):
            return 0 <= x < self.board_size and 0 <= y < self.board_size

        # iterate over the 5x5 board
        for i in range(self.board_size):
            for j in range(self.board_size):
                if board[i][j] == 0:

                    # define the 8 directions to check
                    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

                    valid = True
                    for dx, dy in directions:

                        # check one step in one direction for a 1
                        x, y = i + dx, j + dy
                        if is_inbound(x, y) and board[x][y] == 1:

                            # check opposite direction for a 1
                            x, y = i - dx, j - dy
                            if is_inbound(x, y) and board[x][y] == 1:
                                valid = False
                                break

                            # check two steps in original direction for a 1
                            x, y = i + 2 * dx, j + 2 * dy
                            if is_inbound(x, y) and board[x][y] == 1:
                                valid = False
                                break

                    if valid: moves.append((i, j))

        return moves

    # returns the next state given a state and a move
    def result(self, state, move):
        i, j = move
        board = deepcopy(state.board)
        board[i][j] = 1
        return GameState(
            to_move=('Min' if state.to_move == 'Max' else 'Max'),
            utility=0,
            board=board,
            moves=self.getmoves(board)
        )

    # returns the utility value of a state
    def utility(self, state, player):
        if state.to_move == 'Max': return -self.value
        else: return self.value

    # returns the utility value of a state
    def evaluation(self, state):
        num_moves = -1 if len(state.moves) == 0 else len(state.moves)
        if state.to_move == 'Max': return self.value/num_moves
        else: return -self.value/num_moves

    # returns true if the state is a terminal state
    def terminal_test(self, state):
        return not self.actions(state)

    # displays board to console
    def display(self, state):
        print("board:")
        for row in state.board:
            print(row)


if __name__ == "__main__":
    #setting up the board
    #this is a 2d array in which 0's are considered empty space and 1's are X's or occupied space
    row = 12
    col = 12
    empty_board = [[0 for i in range(col)] for j in range(row)]

    notakto = Notakto(board=empty_board)  # Creating the game instance
    # print(Notakto.board_size)
    utility = notakto.play_game(alpha_beta_cutoff_player, alpha_beta_cutoff_player) # computer moves first
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
