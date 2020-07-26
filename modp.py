#!/usr/bin/env python3

import numpy as np

class Board:
    def __init__(self, board_size, p):
        self.board = np.zeros(board_size, dtype=int)
        self.p = p

    def sum_line(self, v):
        inds = np.where((v[:-1] - v[1:] == 0) & (v[:-1] != 0))
        v[inds] = v[inds] * 2 % self.p
        v[inds[0][:] + 1] = 0
        return np.concatenate((v[v != 0], v[v == 0]))


board = Board((4, 4), 5)
board.board[2, 2] = 2
board.board[2, 0] = 2
board.board[2, 3] = 4
print(board.board)
print(board.sum_left())
