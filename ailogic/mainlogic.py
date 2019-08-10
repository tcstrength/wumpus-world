from entities.statustypes import *
from entities.directions import *
from ailogic.process import *
import time

def main(gamemap, gamecontrol, move):
    process = Process(gamemap)
    # s = chr(gamemap.find_agent()[0] + 48) + ',' + chr(gamemap.find_agent()[1] + 48)
    # process.PossibleMove(s)
    
    if(not move):
        move = process.CalculateMove()
        print(move)
    if(move and move[0] is None):
        return
    s = move[0]
    move_next = s.split(',')
    y = int(move_next[0])
    x = int(move_next[1])
    row,col = gamecontrol.move(y,x)
    # row,col = gamecontrol.move(RIGHT)
    gamemap.open(row, col)
    
    if (gamemap.has_status(row, col, STENCH)):
        print("STENCH")
    if (gamemap.has_status(row, col, BREEZE)):
        print("Breeze")
    if (gamemap.has_status(row, col, GOLD)):
        print("GOLD")
    if (gamemap.has_status(row, col, PIT)):
        print("PIT")
    if (gamemap.has_status(row, col, WUMPUS)):
        print("WUMPUS")
    time.sleep(0.5)
