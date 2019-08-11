from entities.statustypes import *
from entities.gamemap import *
import random
from ailogic.KB import KB
class Process:
    def __init__(self, map):
        self.history_move = ""
        self.map = map
        self.KB = KB()
    # cac array: ['y,x', 'y,x',...], string: 'y,x'
    # Tinh cac buoc co the di dc    
    def PossibleMove(self, str):
        temp = str.split(',')
        y = int(temp[0])
        x = int(temp[1])
        arrMove = []
        if(x - 1 >= 0):
            posX = x - 1
            posY = y
            s = chr(posY + 48) + ',' + chr(posX + 48)
            if(self.map.has_status(posY, posX, PIT) == False and self.map.has_status(posY, posX, WUMPUS) == False):
                arrMove.append(s)
        if(x + 1 <= 9):
            posX = x + 1
            posY = y 
            s = chr(posY + 48) + ',' + chr(posX + 48)
            if(self.map.has_status(posY, posX, PIT) == False and self.map.has_status(posY, posX, WUMPUS) == False):
                arrMove.append(s)
        if(y - 1 >= 0):
            posX = x
            posY = y - 1 
            s = chr(posY + 48) + ',' + chr(posX + 48)
            if(self.map.has_status(posY, posX, PIT) == False and self.map.has_status(posY, posX, WUMPUS) == False):
                arrMove.append(s)
        if(y + 1 <= 9):
            posX = x
            posY = y + 1
            s =  chr(posY + 48) + ',' + chr(posX + 48)
            if(self.map.has_status(posY, posX, PIT) == False and self.map.has_status(posY, posX, WUMPUS) == False):
                arrMove.append(s)
        
        return arrMove
    
    # Nay t eo hieu lam
    def MoveLoop(self, cur, dist):
        temp = cur.split(',')
        cur_y = int(temp[0])
        cur_x = int(temp[1])
        temp = dist.split(',')
        dist_y = int(temp[0])
        dist_x = int(temp[1])
        res = []
        while(dist != cur):
            move = self.PossibleMove(dist)
            move.sort()
            for s in move:
                #if(s not in self.KB.visited or s in res):
                if(self.KB.visited.count(s) == 0 or res.count(s) > 0):
                    move.remove(s)
            if(len(move) > 1):
                for s in move:
                    temp = s.split(',')
                    t_y = int(temp[0])
                    t_x = int(temp[1])
                    if((abs(t_x - cur_x) + abs(t_y - cur_y)) < (abs(dist_x - cur_x) + abs(dist_y - cur_y))):
                        dist_x = t_x
                        dist_y = t_y
                        res.append(s)
                        dist = s
                        break
                    # else:
                    #     continue
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
    
    # Tim vi tri gan nhat co the di duoc
    def FindNearest(self, cur):
        temp = cur.split(',')
        y = int(temp[0])
        x = int(temp[1])
        temp = self.KB.safe[0].split(',')
        dist_y = int(temp[0])
        dist_x = int(temp[1])
        
        Max = abs(dist_x - x) + abs(dist_y - y)
        res = self.KB.safe[0]
        for s in self.KB.safe:
            temp = s.split(',')
            temp_y = int(temp[0])
            temp_x = int(temp[1])
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
        # Check xem cur pos là ô trống k có dấu hiệu/vàng
        if(self.map.has_status(y, x, STENCH) == False and self.map.has_status(y, x, BREEZE) == False and self.map.has_status(y, x, GOLD) == False):
            next_move = self.PossibleMove(pos)
            for s in next_move:
                if(self.KB.visited.count(s) > 0):
                # if(s in self.KB.visited):
                    next_move.remove(s)
                else:
                    #if(s not in self.KB.safe):
                    if(self.KB.safe.count(s) == 0):
                        self.KB.safe.append(s)
                        
            if(len(next_move) > 0):
                move = next_move[random.randrange(len(next_move))] # chon buoc di ngau nhien
                res.append(move)
                self.KB.visited.append(move)
                while(self.KB.safe.count(move) > 0): #move in self.KB.safe
                    self.KB.safe.remove(move)
                    
                self.history_move = pos
            else:
                if(len(self.KB.safe) != 0):
                    res = self.MoveLoop(pos, self.FindNearest(pos))
                    # if(len(res) == 0):
                    #     self.history_move = ""
                    # elif(len(res) == 1):
                    #     self.history_move = res[0]
                    # else:
                    self.history_move = res[len(res) - 2]
                        
            return res
        
        if(self.map.has_status(y, x, GOLD)):
            res.append(pos)                    
            return res
        else:
            next_move = self.PossibleMove(pos)
            percept = ""
            
            if (self.map.has_status(y, x, STENCH)):
                local = chr(y + 48) + ',' + chr(x + 48)
                self.KB.addStench(local)
            if (self.map.has_status(y, x, BREEZE)):
                local = chr(y + 48) + ',' + chr(x + 48)
                self.KB.addBreeze(local)
            
            self.KB.visited.append(pos)
            for s in next_move:
                #if(s in self.KB.visited):
                if(self.KB.visited.count(s) > 0):
                    next_move.remove(s)
            
            for s in next_move:
                # if(s in self.KB.safe):
                if(self.KB.safe.count(s) > 0):
                    self.KB.visited.append(s)
                    #while(s in self.KB.safe):
                    while(self.KB.safe.count(s) > 0):
                        self.KB.safe.remove(s)
                    self.history_move = pos
                    res.append(s)
                    return res
            
            res.append(self.history_move)
            self.history_move = pos
            return res
        
            
        