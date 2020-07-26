#!/usr/bin/env python3

import numpy as np

class Board:
    def __init__(self, shape, p):
        self.shape = shape
        self.board = np.zeros(shape, dtype=int)
        self.p = p


    def sum_left(self, v):
        nums = v[v != 0]
        inds = np.where(nums[:-1] - nums[1:] == 0)
        nums[inds] = nums[inds] * 2 % self.p
        nums = np.delete(nums, inds[0][:] + 1)
        return np.concatenate((nums, np.zeros(v.size - nums.size)))

    def sum_right(self, v):
        nums = v[v != 0]
        inds = np.where(nums[:-1] - nums[1:] == 0)
        nums[inds] = nums[inds] * 2 % self.p
        nums = np.delete(nums, inds[0][:] + 1)
        return np.concatenate((np.zeros(v.size - nums.size), nums))

    def move_left(self):
        for i in range(self.shape[0]):
            self.board[i, :] = self.sum_left(self.board[i, :])

    def move_up(self):
         for i in range(self.shape[1]):
            self.board[:, i] = self.sum_left(self.board[:, i])

    def move_right(self):
        for i in range(self.shape[0]):
            self.board[i, :] = self.sum_right(self.board[i, :])

    def move_down(self):
        for i in range(self.shape[1]):
            self.board[:, i] = self.sum_right(self.board[:, i])

board = Board((4, 4), 5)
board.board[2, 2] = 2
board.board[1, 1] = 3
board.board[0, 1] = 3
board.board[0, 2] = 2
board.board[2, 0] = 2
board.board[1, 2] = 1
board.board[2, 3] = 4

print(board.board)
board.move_down()
print(board.board)
