#!/usr/bin/env python3

import pygame as pg
import modp


class Gboard(modp.Board):
    def __init__(self, shape, p):
        self.colors = {
            0: (46, 52, 64),
            1: (191, 97, 106),
            2: (136, 192, 208),
            3: (163, 190, 140),
            4: (94, 129, 172),
            5: (180, 142, 173),
            6: (235, 203, 139),
            7: (208, 135, 112),
            8: (142, 188, 187)
        }
        self.font_color = ()
        self.font = pg.font.SysFont("Iosevka Term Bold", 42)
        self.screen_shape = (800, 800)
        self.screen = pg.display.set_mode(self.screen_shape)
        super().__init__(shape, p)

    def draw(self):
        tile_size = 200
        pg.draw.rect(self.screen, (67, 76, 94), (0, 0, 800, 800))
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                x_pos = j * 200
                y_pos = i * 200
                pg.draw.rect(self.screen, self.colors[self.board[i, j]], (x_pos + 2, y_pos + 2, 198, 198))
                if self.board[i, j] != 0:
                    txt_surf = self.font.render(str(self.board[i, j]), True, (40, 40, 20))
                    self.screen.blit(txt_surf, (x_pos + 92, y_pos + 88))
