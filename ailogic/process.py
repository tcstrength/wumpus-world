from entities.statustypes import *
import random

class Process:
    def __init__(self, map):
        self.history_move = ""
        self.map = map
        
    def PossibleMove(self, str):
        temp = str.split(',')
        y = int(temp[0])
        x = int(temp[1])
        s = ""
        arrMove = []
        actionMove = []
        if(x - 1 >= 0):
            posX = x - 1
            posY = y
            s =  chr(posX + 48) + ',' + chr(posY + 48)
            if(self.map.has_status(posY, posX, WUMPUS) == False and self.map.has_status(posY, posX, PIT) == False):
                arrMove.append(s)
        if(x + 1 <= 9):
            posX = x + 1
            posY = y 
            s =  chr(posX + 48) + ',' + chr(posY + 48)
            if(self.map.has_status(posY, posX, WUMPUS) == False and self.map.has_status(posY, posX, PIT) == False):
                arrMove.append(s)
        if(y - 1 >= 0):
            posX = x
            posY = y - 1 
            s =  chr(posX + 48) + ',' + chr(posY + 48)
            if(self.map.has_status(posY, posX, WUMPUS) == False and self.map.has_status(posY, posX, PIT) == False):
                arrMove.append(s)
        if(y + 1 <= 9):
            posX = x
            posY = y + 1
            s =  chr(posX + 48) + ',' + chr(posY + 48)
            if(self.map.has_status(posY, posX, WUMPUS) == False and self.map.has_status(posY, posX, PIT) == False):
                arrMove.append(s)
        
        print(arrMove)
        return arrMove
    
    # def MoveLoop(self, cur, dist):
    #     temp = cur.split(',')
    #     cur_y = int(temp[0])
    #     cur_x = int(temp[1])
    #     temp = dist.split(',')
    #     dist_y = int(temp[0])
    #     dist_x = int(temp[1])
    #     s = ""
    #     move = ""
    #     res = ""
    #     while(dist != cur):
    #         move = self.PossibleMove(dist)
    #         move.sort()
    #         for s in move:
                
        
    # def CalculateMove(self):
    #     r = random.randint(0, 5)
    #     temp = str.split(',')
    #     y = int(temp[0])
    #     x = int(temp[1])
    #     s = ""
        