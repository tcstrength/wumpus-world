print("Test vang ke ben")
print("Test kho hon xiu")
print("Khong co vang luon")
print("1 hang` pits khong cho di qua")

import pygame
from resources.data import gamedata
from entities.modelbox import ModelBox
from graphics.window import Window
from graphics.grid import Grid
from graphics.gameboard import GameBoard
from graphics.pit import Pit
from graphics.archer import Archer

pygame.init()

window = Window("Wumpus World", gamedata.get_rows() * 64, gamedata.get_cols() * 64)
window.background = "background.png"
board = GameBoard(gamedata.get_rows(), gamedata.get_cols())
board.add_model(Pit(), 1, 0)
board.add_model(Archer(), 0, 0)

while (window.running):
    window.begin()
    board.draw(window)
    window.end()

pygame.quit()