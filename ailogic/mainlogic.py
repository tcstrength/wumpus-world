from entities.statustypes import *
from entities.directions import *
import time

def main(gamemap, gamecontrol, move, process):
    if(len(move) == 0):
        move = process.CalculateMove()
    if(len(move) != 0 and move[0] ==""):
        return
    
    print(move)
    s = move[0]
    move_next = s.split(',')
    y = int(move_next[0])
    x = int(move_next[1])
    row,col = gamecontrol.move(y,x)
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
