from entities.statustypes import *
from entities.directions import *
import time

def main(gamemap, gamecontrol):
    row,col = gamecontrol.move(RIGHT)
    if (gamemap.has_status(row, col, STENCH)):
        print("STENCH")
    time.sleep(1)