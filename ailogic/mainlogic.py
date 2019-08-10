from entities.statustypes import *
from entities.directions import *
from ailogic.process import *
import time

def main(gamemap, gamecontrol):
    process = Process(gamemap)
    s = chr(gamemap.find_agent()[0] + 48) + ',' + chr(gamemap.find_agent()[1] + 48)
    process.PossibleMove(s)
    
    row,col = gamecontrol.move(RIGHT)
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
