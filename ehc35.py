import math
import random
import time

import game
import othello

class ehc35(game.Player):
    def __init__(self, time_limit_ms):
        self.time_limit_ms = time_limit_ms

    def choose_move(self, state):
        start_time = time.time()
        best_move = None
        depth = 1

        while (time.time() - start_time) * 1000 < self.time_limit_ms - 10: 
            try:
                best_move = self.iterative_deepening_alphabeta(state, depth, start_time)
                depth += 1
            except TimeoutError:
                break

        return best_move

    def iterative_deepening_alphabeta(self, state, depth, start_time):
        best_move = None
        best_value = -math.inf if state.nextPlayerToMove == othello.PLAYER1 else math.inf
        alpha = -math.inf
        beta = math.inf

        moves = state.generateMoves()
        if not moves:
            return None

        for move in moves:
            if (time.time() - start_time) * 1000 > self.time_limit_ms:
                raise TimeoutError()

            new_state = state.applyMoveCloning(move)
            value = self.alphabeta(new_state, depth - 1, alpha, beta, start_time)

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

    def alphabeta(self, state, depth, alpha, beta, start_time):
        if (time.time() - start_time) * 1000 > self.time_limit_ms:
            raise TimeoutError()

        if depth == 0 or state.game_over():
            return self.evaluate(state)

        if state.nextPlayerToMove == othello.PLAYER1:
            best_value = -math.inf
            moves = state.generateMoves()
            if not moves:
                return self.evaluate(state)
            for move in moves:
                new_state = state.applyMoveCloning(move)
                best_value = max(best_value, self.alphabeta(new_state, depth - 1, alpha, beta, start_time))
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break
            return best_value
        else:
            best_value = math.inf
            moves = state.generateMoves()
            if not moves:
                return self.evaluate(state)
            for move in moves:
                new_state = state.applyMoveCloning(move)
                best_value = min(best_value, self.alphabeta(new_state, depth - 1, alpha, beta, start_time))
                beta = min(beta, best_value)
                if beta <= alpha:
                    break
            return best_value

    def evaluate(self, state):
        score = state.score()

        board_size = state.boardSize
        corner_value = 10
        edge_value = 3

        for i in [0, board_size - 1]:
            for j in [0, board_size - 1]:
                if state.board[i][j] == othello.PLAYER1:
                    score += corner_value
                elif state.board[i][j] == othello.PLAYER2:
                    score -= corner_value

        for i in range(1, board_size - 1):
            if state.board[0][i] == othello.PLAYER1 or state.board[board_size-1][i] == othello.PLAYER1 :
                score += edge_value
            elif state.board[0][i] == othello.PLAYER2 or state.board[board_size-1][i] == othello.PLAYER2 :
                score -= edge_value

            if state.board[i][0] == othello.PLAYER1 or state.board[i][board_size - 1] == othello.PLAYER1:
                score += edge_value
            elif state.board[i][0] == othello.PLAYER2 or state.board[i][board_size - 1] == othello.PLAYER2:
                score -= edge_value
        return score

