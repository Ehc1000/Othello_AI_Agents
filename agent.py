import math
import random

import game
import othello

class HumanPlayer(game.Player):

    def __init__(self):
        super().__init__()

    def choose_move(self, state):
        # generate the list of moves:
        moves = state.generateMoves()

        for i, action in enumerate(moves):
            print('{}: {}'.format(i, action))
        response = input('Please choose a move: ')
        return moves[int(response)]

class RandomAgent(game.Player):
    def choose_move(self, state):
        moves = state.generateMoves()
        if moves:
            return random.choice(moves)
        else:
            return None


class MinimaxAgent(game.Player):
    def __init__(self, depth):
        self.depth = depth

    def choose_move(self, state):
        best_move = None
        best_value = -math.inf if state.nextPlayerToMove == othello.PLAYER1 else math.inf

        moves = state.generateMoves()
        if not moves:
            return None

        for move in moves:
            new_state = state.applyMoveCloning(move)
            value = self.minimax(new_state, self.depth - 1)

            if state.nextPlayerToMove == othello.PLAYER1:
                if value > best_value:
                    best_value = value
                    best_move = move
            else:
                if value < best_value:
                    best_value = value
                    best_move = move

        return best_move

    def minimax(self, state, depth):
        if depth == 0 or state.game_over():
            return state.score()

        if state.nextPlayerToMove == othello.PLAYER1:
            best_value = -math.inf
            moves = state.generateMoves()
            if not moves:
                return state.score()
            for move in moves:
                new_state = state.applyMoveCloning(move)
                best_value = max(best_value, self.minimax(new_state, depth - 1))
            return best_value
        else:
            best_value = math.inf
            moves = state.generateMoves()
            if not moves:
                return state.score()
            for move in moves:
                new_state = state.applyMoveCloning(move)
                best_value = min(best_value, self.minimax(new_state, depth - 1))
            return best_value

class AlphaBeta(game.Player):
    def __init__(self, depth):
        self.depth = depth

    def choose_move(self, state):
        best_move = None
        best_value = -math.inf if state.nextPlayerToMove == othello.PLAYER1 else math.inf
        alpha = -math.inf
        beta = math.inf

        moves = state.generateMoves()
        if not moves:
            return None

        for move in moves:
            new_state = state.applyMoveCloning(move)
            value = self.alphabeta(new_state, self.depth - 1, alpha, beta)

            if state.nextPlayerToMove == othello.PLAYER1:
                if value > best_value:
                    best_value = value
                    best_move = move
                alpha = max(alpha, best_value)
            else:
                if value < best_value:
                    best_value = value
                    best_move = move
                beta = min(beta, best_value)

        return best_move

    def alphabeta(self, state, depth, alpha, beta):
        if depth == 0 or state.game_over():
            return state.score()

        if state.nextPlayerToMove == othello.PLAYER1:
            best_value = -math.inf
            moves = state.generateMoves()
            if not moves:
                return state.score()
            for move in moves:
                new_state = state.applyMoveCloning(move)
                best_value = max(best_value, self.alphabeta(new_state, depth - 1, alpha, beta))
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break
            return best_value
        else:
            best_value = math.inf
            moves = state.generateMoves()
            if not moves:
                return state.score()
            for move in moves:
                new_state = state.applyMoveCloning(move)
                best_value = min(best_value, self.alphabeta(new_state, depth - 1, alpha, beta))
                beta = min(beta, best_value)
                if beta <= alpha:
                    break
            return best_value

