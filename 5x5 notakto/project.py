from games import *
from copy import deepcopy
import random
# import logging    # first of all import the module

# logging.basicConfig(filename='debug.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
# logging.warning('This message will get logged on to a file')

class Notakto(Game):
    def __init__(self, board):
        self.initial = GameState(to_move='Max', utility=0, board=board, moves=self.getmoves(board))

    #actions left over from game of nim, may need rework
    def actions(self, state):
        return state.moves.copy()

    #move creation finished
    # def getmoves(self, board):
    #     moves = []
    #     for i in range(5):  #for each row
    #         for j in range(5):  #for each col
    #             if board[i][j] == 0:    #if space is empty
    #                 moves.append([i,j]) #add x and y cords to the moves array
    #     #printing moves and board, used for debugging
    #     # print(moves)
    #     # for row in board:
    #     #     print(row)
    #     # random.shuffle(moves)
    #     return moves

    #the revised getmoves returns non losing moves only loosing move is defined as a move that would result in three 1's in a row in all directions including diagonals
    def getmoves(self, board):
    # Initialize the valid positions list
        moves = []

        # Iterate over the 5x5 board
        for i in range(5):
            for j in range(5):
                if board[i][j] == 0:
                    # Check all eight directions for two consecutive 1s and a 1 separated by space
                    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
                    valid = True
                    for dx, dy in directions:
                        count = 0
                        for step in range(1, 3):
                            x, y = i + step * dx, j + step * dy
                            if 0 <= x < 5 and 0 <= y < 5 and board[x][y] == 1:
                                count += 1
                            else:
                                break
                        # Check for a separated 1 in both directions
                        next_x, next_y = i + 3 * dx, j + 3 * dy
                        if count == 2 or (count == 1 and 0 <= next_x < 5 and 0 <= next_y < 5 and board[next_x][next_y] == 1):
                            valid = False
                            break
                    if valid:
                        moves.append((i, j))

        return moves

    # def getmoves(self, board):
    # # Initialize the valid positions list
    #     moves = []

    #     # Iterate over the 5x5 board
    #     for i in range(5):
    #         for j in range(5):
    #             if board[i][j] == 0:
    #                 # Check all eight directions for two consecutive 1s and a 1 separated by space
    #                 directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    #                 valid = True
    #                 for dx, dy in directions:
    #                     count_forward = 0
    #                     count_backward = 0
    #                     for step in range(1, 3):
    #                         x_forward, y_forward = i + step * dx, j + step * dy
    #                         x_backward, y_backward = i - step * dx, j - step * dy
    #                         if 0 <= x_forward < 5 and 0 <= y_forward < 5 and board[x_forward][y_forward] == 1:
    #                             count_forward += 1
    #                         if 0 <= x_backward < 5 and 0 <= y_backward < 5 and board[x_backward][y_backward] == 1:
    #                             count_backward += 1
    #                     if count_forward == 2 or count_backward == 2 or (count_forward == 1 and count_backward == 1):
    #                         valid = False
    #                         break
    #                 if valid:
    #                     moves.append((i, j))
    #     return moves

    # def getmoves(self, board):
    #     # Initialize the valid positions list
    #     moves = []

    #     # Iterate over the 5x5 board
    #     for i in range(5):
    #         for j in range(5):
    #             if board[i][j] == 0:
    #                 # Check all eight directions for two consecutive 1s and a 1 separated by space
    #                 directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    #                 valid = True
    #                 for dx, dy in directions:
    #                     # Check for two consecutive 1s
    #                     count_consecutive = 0
    #                     for step in range(1, 3):
    #                         x, y = i + step * dx, j + step * dy
    #                         if 0 <= x < 5 and 0 <= y < 5 and board[x][y] == 1:
    #                             count_consecutive += 1
    #                         else:
    #                             break
    #                     # Check for a separated 1 in both directions
    #                     x_before, y_before = i - dx, j - dy
    #                     x_after, y_after = i + 3 * dx, j + 3 * dy
    #                     if count_consecutive == 2 or ((0 <= x_before < 5 and 0 <= y_before < 5 and board[x_before][y_before] == 1) and (0 <= x_after < 5 and 0 <= y_after < 5 and board[x_after][y_after] == 1)):
    #                         valid = False
    #                         break
    #                 if valid:
    #                     moves.append((i, j))

    #     return moves

    # def getmoves(self, board):
    # # Initialize the valid positions list
    #     moves = []

    #     # Iterate over the 5x5 board
    #     for i in range(5):
    #         for j in range(5):
    #             if board[i][j] == 0:
    #                 # Check all eight directions for two consecutive 1s and a 1 separated by space
    #                 directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    #                 valid = True
    #                 for dx, dy in directions:
    #                     # Check for three consecutive 1s including current position
    #                     count_consecutive = 0
    #                     for step in [-1, 1, 2]:
    #                         x, y = i + step * dx, j + step * dy
    #                         if 0 <= x < 5 and 0 <= y < 5 and board[x][y] == 1:
    #                             count_consecutive += 1
    #                         else:
    #                             break
    #                     if count_consecutive >= 2:
    #                         valid = False
    #                         break
    #                 if valid:
    #                     moves.append((i, j))

    #     return moves




    #result updated finished - needs testing
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

    #utility works
    def utility(self, state, player):
        if state.to_move == 'Max': return -25
        else: return 25

    def evaluation(self, state):
        num_moves = -1 if len(state.moves) == 0 else len(state.moves)
        if state.to_move == 'Max': return 25/num_moves
        else: return -25/num_moves

    #terminal test
    def terminal_test(self, state):
        return not self.actions(state)

    #cutoff test
    # def cutoff_test(self, state, depth):
    #     return self.is_loose_condition(state) or depth > 4 or self.terminal_test(state)

    #currently unused
    def is_loose_condition(self, state):
        # check for loosing condition
        for i in range(5):  #for each row
            for j in range(5):  #for each col
                #detect if X is there
                if state.board[i][j] == 1:
                    #checking backwards diagonal
                    # 0 0 1
                    # 0 1 0
                    # 1 0 0
                    if j > 1 and i < 3 and state.board[i+1][j-1] == 1 and state.board[i+2][j-2] == 1:
                        return True
                    #checking vertical down
                    # 0 1 0
                    # 0 1 0
                    # 0 1 0
                    if i < 3 and state.board[i+1][j] == 1 and state.board[i+2][j] == 1:
                        return True
                    #checking diagonal down
                    # 1 0 0
                    # 0 1 0
                    # 0 0 1
                    if i < 3 and j < 3 and state.board[i+1][j+1] == 1 and state.board[i+2][j+2] == 1:
                        return True
                    #checking horizontal
                    # 1 1 1
                    # 0 0 0
                    # 0 0 0
                    if j < 3 and state.board[i][j+1] == 1 and state.board[i][j+2] == 1:
                        return True
        #if no match return false
        return False

    #left over display function, may or may not be working
    def display(self, state):
        print("board:")
        for row in state.board:
            print(row)

#main, might need work for proper implemenetation
if __name__ == "__main__":
    #setting up the board
    #this is a 2d array in which 0's are considered empty space and 1's are X's or occupied space
    row = 5
    col = 5
    empty_board = [[0 for i in range(col)] for j in range(row)]

    board = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [1,1,1,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]

    board2 = [
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1]
    ]

    notakto = Notakto(board=empty_board)  # Creating the game instance
    # print(notakto.getmoves(board2))
    utility = notakto.play_game(alpha_beta_cutoff_player, alpha_beta_cutoff_player) # computer moves first
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
