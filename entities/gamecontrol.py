from graphics.gameboard import GameBoard
from entities.statustypes import AGENT
from entities.directions import DIRECTIONS

class GameControl:
    def __init__(self, gamemap):
        self.gamemap = gamemap

    def move(self, direction):
        row, col = self.gamemap.find_agent()
        directionCoord = DIRECTIONS[direction]
        nextrow = row + directionCoord[1]
        nextcol = col + directionCoord[0]

        if (self.gamemap.is_legal(nextrow, nextcol) == False):
            return [row, col]

        self.gamemap.del_status(row, col, AGENT)
        self.gamemap.add_status(nextrow, nextcol, AGENT)
        return [nextrow, nextcol]


