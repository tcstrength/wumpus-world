print("Test vang ke ben")
print("Test kho hon xiu")
print("Khong co vang luon")
print("1 hang` pits khong cho di qua")

import pygame
from resources.data import gamedata
from entities.modelbox import ModelBox
from entities.gamemap import GameMap
from entities.gamecontrol import GameControl
from graphics.window import Window
from graphics.gameboard import GameBoard
from graphics.models.archer import Archer
from graphics.models.pit import Pit
from graphics.models.wumpus import Wumpus
from ailogic import mainlogic

pygame.init()

window = Window("Wumpus World", gamedata.get_rows() * 64, gamedata.get_cols() * 64)
window.background = "background.png"
gamemap = GameMap(10, 10)
gamemap.load_map("maps/map1.txt")
gamecontrol = GameControl(gamemap)
board = GameBoard(gamemap)
move = []
while (window.running):
    window.begin()
    mainlogic.main(gamemap, gamecontrol, move)
    board.draw(window)
    window.end()

pygame.quit()