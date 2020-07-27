#!/usr/bin/env python3

import numpy as np

class Board:
    def __init__(self, shape, p):
        self.shape = shape
        self.board = np.zeros(shape, dtype=int)
        self.p = p
        self.score = 0

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

    def get_score(self):
        self.score = np.sum(self.board)

    def new_tile(self):
        inds = np.where(self.board == 0)
        rand_ind = np.random.randint(inds[0].size)
        tile_ind = np.array(inds)[:, rand_ind]
        self.board[tile_ind[0], tile_ind[1]] = 2

    def check_loss(self):
        ver_diff = self.board[1:, :] - self.board[:-1, :]
        hor_diff = self.board[:, 1:] - self.board[:, :-1]
        if 0 in ver_diff or 0 in hor_diff:
            return False
        else:
            return True
