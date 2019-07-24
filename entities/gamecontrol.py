from graphics.gameboard import GameBoard
from entities.statustypes import AGENT

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


