from graphics.gameboard import GameBoard
from entities.types import *

LEFT = 0
TOP = 1
RIGHT = 2
BOTTOM = 3

DIRECTIONS = {
    LEFT: [-1, 0],
    TOP: [0, -1],
    RIGHT: [1, 0],
    BOTTOM: [0, 1]
}

class GameControl:
    def __init__(self, gameboard):
        self.gameboard = gameboard

    def move(self, direction):
        row, col = self.gameboard.find_agent()
        self.gameboard.del_status(row, col, AGENT)
        row += direction[1]
        col += direction[0]
        self.gameboard.add_status(row, col, AGENT)
        return [row, col]


