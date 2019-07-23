print("Test vang ke ben")
print("Test kho hon xiu")
print("Khong co vang luon")
print("1 hang` pits khong cho di qua")

import pygame
from entities.modelbox import ModelBox
from graphics.window import Window
from graphics.grid import Grid
from graphics.gameboard import GameBoard
from graphics.pit import Pit
from graphics.archer import Archer

pygame.init()

window = Window("Wumpus World", 640, 640)
window.background = "background.png"
grid = Grid()
board = GameBoard(10, 10)
board.add_model(Pit(), 1, 0)
board.add_model(Archer(), 0, 0)

while (window.running):
    window.begin()
    board.draw(window)
    grid.draw(window)
    window.end()

pygame.quit()