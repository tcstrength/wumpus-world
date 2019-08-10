from entities.statustypes import *
from entities.gamemap import *
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
                temp_y = int(s[0])
                temp_x = int(s[1])
                if(self.map.cell_table[temp_y][temp_x].closed == False or res.__contains__(s)):
                    move.remove(s)
            if(move.__len__ > 1):
                for s in move:
                    temp = s.split(',')
                    t_y = int(temp[0])
                    t_x = int(temp[1])
                    if(abs(t_x - cur_x) + abs(t_y - cur_y) < abs(dist_x - cur_x + abs(dist_y - cur_y))):
                        dist_x = t_x
                        dist_y = t_y
                        res.append(s)
                        dist = s
                        break
            
            else:
                temp = move[0].split(',')
                t_y = int(temp[0])
                t_x = int(temp[1])
                dist = move[0]
                dist_x = t_x
                dist_y = t_y
                res.append(move[0])
                
        res.reverse()
        return res
                    
    def FindNearest(self, cur):
        temp = cur.split(',')
        x = int(temp[1])
        y = int(temp[0])
        temp = self.map.Safe[0].split(',')
        dist_x = temp[1]
        dist_y = temp[0]
        Max = abs(dist_x - x) + abs(dist_y - y)
        res = self.map.Safe[0]
        for s in self.map.Safe:
            temp = s.split(',')
            temp_x = int(temp[1])
            temp_y = int(temp[0])
            value = abs(temp_x - x) + abs(temp_y - y)
            if(Max > value):
                res = s
                Max = value
                dist_x = temp_x
                dist_y = temp_y
        
        return res
        
    def CalculateMove(self):
        y, x = self.map.find_agent()
        pos = chr(y + 48) + ',' + chr(x + 48)
        res = []
        if(self.map.has_status(y, x, AGENT)):
            next_move = self.PossibleMove(pos)
            for s in next_move:
                if(self.map.Visited.__contains__(s)):
                    next_move.remove(s)
                else:
                    if(self.map.Safe.__contains__(s) == False):
                        self.map.Safe.append(s)
                        
            if(next_move.count != 0):
                move = next_move[random.randint(0, len(next_move) - 1)]
                res.append(move)
                self.map.Visited.append(move)
                while(self.map.Safe.__contains__(move)):
                    self.map.Safe.remove(move)
                self.history_move = pos
            else:
                if(self.map.Safe.count != 0):
                    res = MoveLoop(pos, FindNearest(pos))
                    self.history_move = res[res.count - 2]
            return res
        
        if(self.map.has_status(y, x, GOLD)):
            res.append(pos)                    
            return res
        else:
            percept = ""
            next_move = self.PossibleMove(pos)
            if (self.map.has_status(y, x, STENCH)):
                percept += "STENCH"
            if (self.map.has_status(y, x, BREEZE)):
                percept += "Breeze"
            self.map.Visited.append(pos)
            for s in next_move:
                if(self.map.Visited.__contains__(s)):
                    next_move.remove(s)
            for s in next_move:
                if(self.map.Safe.__contains__(s)):
                    self.map.Visited.append(s)
                    while(self.map.Safe.__contains__(s)):
                        self.map.Safe.remove(s)
                    self.history_move = pos
                    res.append(s)
                    return res
            res.append(self.history_move)
            
            self.history_move = pos
            return res
            
            
        