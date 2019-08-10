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
    
    def MoveLoop(self, cur, dist):
        temp = cur.split(',')
        cur_y = int(temp[0])
        cur_x = int(temp[1])
        temp = dist.split(',')
        dist_y = int(temp[0])
        dist_x = int(temp[1])
        move = ""
        res = []
        while(dist != cur):
            move = self.PossibleMove(dist)
            move.sort()
            for s in move:
                temp_x = int(s[1])
                temp_y = int(s[0])
                if(self.map.cell_table[y][x].closed == False or res.__contains__(s)):
                    move.remove(s)
            if(move.__len__ > 1):
                for s in move:
                    temp = s.split(',')
                    t_x = int(temp[1])
                    t_y = int(temp[0])
                    if(abs(t_x - cur_x) + abs(t_y - cur_y) < abs(dist_x - cur_x + abs(dist_y - cur_y))):
                        dist_x = t_x
                        dist_y = t_y
                        res.append(s)
                        dist = s
                        break
            
            else:
                temp = move[0].split(',')
                t_x = int(temp[1])
                t_y = int(temp[0])
                dist = move[0]
                dist_x = t_x
                dist_y = t_y
                res.append(move[0])
                
        res.reverse()
        return res
                    
    def FindNearest(self, cur):
        safe = self.map.findSafe()[0]
        temp = cur.split(',')
        x = temp[1]
        y = temp[0]
        temp = safe[0].split(',')
        dist_x = temp[1]
        dist_y = temp[0]
        Max = abs(dist_x - x) + abs(dist_y - y)
        res = safe[0]
        for s in safe:
            temp = s.split(',')
            
        
        return res
        
    def CalculateMove(self):
        r = random.randint(0, 5)
        temp = str.split(',')
        y = int(temp[0])
        x = int(temp[1])
        s = ""
        