#!/usr/bin/env python3

import numpy as np

class Board:
    def __init__(self, board_size, p):
        self.board = np.zeros(board_size)
        self.p = p
