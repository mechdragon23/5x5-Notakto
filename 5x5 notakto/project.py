from games import *

class Notakto(Game):
    def __init__(self, board=[]):
        self.initial = GameState(to_move='MIN', utility=0, board=board, moves=self.getmoves(board))

    #actions left over from game of nim, may need rework
    def actions(self, state):
        return state.moves.copy()

    #move creation finished
    def getmoves(self, board):
        moves = []
        for i in range(5):  #for each row
            for j in range(5):  #for each col
                if board[i][j] == 0:    #if space is empty
                    moves.append([i,j]) #add x and y cords to the moves array
        #printing moves and board, used for debugging
        print(moves)
        for row in board:
            print(row)
        return moves

    #result updated finished - needs testing
    def result(self, state, move):
        i, j = move
        board = state.board.copy()
        board[i][j] = 1
        return GameState(
            to_move=('Min' if state.to_move == 'Max' else 'Max'),
            utility=0,
            board=board,
            moves=self.getmoves(board)
        )

    #utility function, non functional, needs rework
    def utility(self, state, player):
        if(player == 'MIN'):
            return -1
        else:
            return 1

    #terminal test finished
    def terminal_test(self, state):
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
    arr = [[0 for i in range(col)] for j in range(row)]

    nim = Notakto(board=arr)  # Creating the game instance
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
