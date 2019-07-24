print("Test vang ke ben")
print("Test kho hon xiu")
print("Khong co vang luon")
print("1 hang` pits khong cho di qua")

import pygame
from resources.data import gamedata
from entities.modelbox import ModelBox
from entities.gamemap import GameMap
from entities.gamecontrol import GameControl
from entities.gamecontrol import DIRECTIONS, LEFT, RIGHT, TOP, BOTTOM
from graphics.window import Window
from graphics.gameboard import GameBoard
from graphics.models.archer import Archer
from graphics.models.pit import Pit
from graphics.models.wumpus import Wumpus
from entities.types import PIT
from entities.types import WUMPUS
from ailogic.mainlogic import main_logic

pygame.init()

window = Window("Wumpus World", gamedata.get_rows() * 64, gamedata.get_cols() * 64)
window.background = "background.png"
gamemap = GameMap(10, 10)
gamemap.load_map("maps/map1.txt")
gamecontrol = GameControl(gamemap)
board = GameBoard(gamemap)

gamecontrol.move(DIRECTIONS[TOP])

while (window.running):
    window.begin()
    main_logic(gamemap, gamecontrol)
    board.draw(window)
    window.end()

pygame.quit()