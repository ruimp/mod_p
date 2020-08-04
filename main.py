#!/usr/bin/env python3

import pygame as pg
import gui

# initialization
pg.font.init()
clock = pg.time.Clock()

# generate board
shape = (4, 4)
p = 9
board = gui.Gboard(shape, p)
board.new_tile()

# main loop
tick_rate = 30
game_over = False
keyup = True
while not game_over:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True

    board.draw()
    pg.display.update()
    clock.tick(tick_rate)

    if event.type == pg.KEYUP:
        keyup = True

    if event.type == pg.KEYDOWN and keyup:
        if event.key == pg.K_LEFT:
            null_move = board.move_left()
            if not null_move:
                board.new_tile()
        elif event.key == pg.K_RIGHT:
            null_move = board.move_right()
            if not null_move:
                board.new_tile()
        elif event.key == pg.K_UP:
            null_move = board.move_up()
            if not null_move:
                board.new_tile()
        elif event.key == pg.K_DOWN:
            null_move = board.move_down()
            if not null_move:
                board.new_tile()
        keyup = False
pg.quit()
quit()
