import random
import numpy as np
from collections import namedtuple, defaultdict
from math import sqrt



GameState = namedtuple('GameState', 'to_move, utility, board, moves')
StochasticGameState = namedtuple('StochasticGameState', 'to_move, utility, board, moves, chance')

# ______________________________________________________________________________
# State Search

def alpha_beta_cutoff_search(state, game, d=4, cutoff_test=None, eval_fn=None):
    """Search game to determine best action; use alpha-beta pruning.
    This version cuts off search and uses an evaluation function."""

    player = game.to_move(state)

    # Functions used by alpha_beta
    def max_value(state, alpha, beta, depth):
        if cutoff_test(state, depth):
            return eval_fn(state)
        v = -np.inf
        for a in game.actions(state):
            v = max(v, min_value(game.result(state, a), alpha, beta, depth + 1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, alpha, beta, depth):
        if cutoff_test(state, depth):
            return eval_fn(state)
        v = np.inf
        for a in game.actions(state):
            v = min(v, max_value(game.result(state, a), alpha, beta, depth + 1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    # Body of alpha_beta_cutoff_search starts here:
    # The default test cuts off at depth d or at a terminal state
    if len(state.moves) == game.value:
        return state.moves[random.randint(0, game.value - 1)]

    cutoff_test = (cutoff_test or (lambda state, depth: depth > d or game.terminal_test(state)))
    eval_fn = eval_fn or (lambda state: game.utility(state, player))
    best_score = -np.inf
    beta = np.inf
    best_action = None
    for a in game.actions(state):
        v = min_value(game.result(state, a), best_score, beta, 1)
        if v > best_score:
            best_score = v
            best_action = a
    return best_action


# ______________________________________________________________________________
# Players for Games

def query_player(game, state):
    """Make a move by querying standard input."""
    print("current state:")
    game.display(state)
    print("available moves: {}".format(game.actions(state)))
    print("")
    move = None
    if game.actions(state):
        move_string = input('Your move? ')
        try:
            move = eval(move_string)
        except NameError:
            move = move_string
    else:
        print('no legal moves: passing turn to next player')
    return move


def AI_silly(game, state):
    """A player that chooses a legal move at random."""
    return random.choice(game.actions(state)) if game.actions(state) else None

def AI_easy(game, state):
    """A player who only thinks one move ahead."""
    return alpha_beta_cutoff_search(state, game, d=1, cutoff_test=None, eval_fn=game.evaluation)

def AI_medium(game, state):
    """A player who thinks few moves ahead, but panics as rushes as board size increases."""
    depth = defaultdict(lambda: 1)
    depth.update({
        5: 4,
        6: 3,
        7: 2,
        8: 2,
    })
    return alpha_beta_cutoff_search(state, game, d=depth[game.board_size], cutoff_test=None, eval_fn=game.evaluation)

def AI_hard(game, state):
    """A player who is more strategic and thinks more moves ahead when as the game progresses."""
    b = round(sqrt(len(state.moves)))
    depth = defaultdict(lambda: 1)
    depth.update({
        4: 5,
        5: 4,
        6: 3,
        7: 2,
        8: 2,
    })
    d = np.inf if b < 4 else depth[b]
    return alpha_beta_cutoff_search(state, game, d=d, eval_fn=game.evaluation)


# ______________________________________________________________________________
# Game Class

class Game:
    """A game is similar to a problem, but it has a utility for each
    state and a terminal test instead of a path cost and a goal
    test. To create a game, subclass this class and implement actions,
    result, utility, and terminal_test. You may override display and
    successors or you can inherit their default methods. You will also
    need to set the .initial attribute to the initial state; this can
    be done in the constructor."""

    def actions(self, state):
        """Return a list of the allowable moves at this point."""
        raise NotImplementedError

    def result(self, state, move):
        """Return the state that results from making a move from a state."""
        raise NotImplementedError

    def utility(self, state, player):
        """Return the value of this final state to player."""
        raise NotImplementedError

    def terminal_test(self, state):
        """Return True if this is a final state for the game."""
        return not self.actions(state)

    def to_move(self, state):
        """Return the player whose move it is in this state."""
        return state.to_move

    def display(self, state):
        """Print or otherwise display the state."""
        print(state)

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    def play_game(self, *players):
        """Play an n-person, move-alternating game."""
        state = self.initial
        while True:
            for player in players:
                move = player(self, state)
                print(f"\nPlayer {state.to_move} {move} n moves: {len(state.moves)}")
                state = self.result(state, move)
                self.display(state)
                if self.terminal_test(state):
                    print(f"\nPlayer {state.to_move} Looses n moves: {len(self.actions(state))}")
                    self.display(state)
                    return self.utility(state, self.to_move(self.initial))
