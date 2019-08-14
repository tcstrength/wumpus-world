from entities.statustypes import *
from entities.gamemap import *
import random
from ailogic.KB import KB
class Process:
    def __init__(self, map):
        self.history_move = ""
        self.map = map
        self.KB = KB()
        y, x = self.map.find_agent()
        pos = chr(y + 48) + ',' + chr(x + 48)
        self.KB.visited.append(pos)
    
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
            moves = self.KB.PossibleMove(dist)
            moves.sort()
            for move in moves:
                #if(s not in self.KB.visited or s in res):
                if(self.KB.visited.count(move) == 0 or res.count(move) > 0):
                    moves.remove(move)
            if(len(moves) > 1):
                for move in moves:
                    temp = move.split(',')
                    t_y = int(temp[0])
                    t_x = int(temp[1])
                    if((abs(t_x - cur_x) + abs(t_y - cur_y)) <= (abs(dist_x - cur_x) + abs(dist_y - cur_y))):
                        dist_x = t_x
                        dist_y = t_y
                        res.append(move)
                        dist = move
                        break
                    # else:
                    #     continue
                if(len(res) == 0):
                    res.append(moves[0])
            else:
                temp = moves[0].split(',')
                t_y = int(temp[0])
                t_x = int(temp[1])
                dist = moves[0]
                dist_x = t_x
                dist_y = t_y
                res.append(moves[0])
                
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
            if(s != self.KB.safe[0]):
                temp = s.split(',')
                temp_y = int(temp[0])
                temp_x = int(temp[1])
                value = abs(temp_x - x) + abs(temp_y - y)
                if(Max >= value):
                    res = s
                    Max = value
                    dist_x = temp_x 
                    dist_y = temp_y - 1
        
        return res
        
    def CalculateMove(self):
        y, x = self.map.find_agent()
        pos = chr(y + 48) + ',' + chr(x + 48)
        res = []
        # Check xem cur pos là ô trống k có dấu hiệu/vàng
        if(self.map.has_status(y, x, STENCH) == False and self.map.has_status(y, x, BREEZE) == False and self.map.has_status(y, x, GOLD) == False):
            next_move = self.KB.PossibleMove(pos)
            for s in next_move:
                if(self.KB.visited.count(s) > 0):
                # if(s in self.KB.visited):
                    next_move.remove(s)
                else:
                    #if(s not in self.KB.safe):
                    if(self.KB.safe.count(s) == 0):
                        self.KB.safe.append(s)
                        if(self.KB.unknown.count(s) > 0):
                            self.KB.unknown.remove(s)
                        if(self.KB.pit.count(s) > 0):
                            self.KB.pit.remove(s)
                        
            if(len(next_move) != 0):
                move = next_move[random.randint(0, len(next_move) - 1)] # chon buoc di ngau nhien
                
                res.append(move)
                self.KB.visited.append(move)
                while(self.KB.safe.count(move) > 0): #move in self.KB.safe
                    self.KB.safe.remove(move)
                    
                self.history_move = pos
            else:
                if(len(self.KB.safe) != 0):
                    res = self.MoveLoop(pos, self.KB.safe[len(self.KB.safe) - 1])
                    self.history_move = res[len(res) - 2]
                        
            return res
        
        if(self.map.has_status(y, x, GOLD)):
            res.append(pos)                    
            return res
        else:
            next_move = self.KB.PossibleMove(pos)
            self.KB.visited.append(pos)
            percept = ""
            
            if (self.map.has_status(y, x, STENCH)):
                local = chr(y + 48) + ',' + chr(x + 48)
                self.KB.addStench(local)
            if (self.map.has_status(y, x, BREEZE)):
                local = chr(y + 48) + ',' + chr(x + 48)
                self.KB.addBreeze(local)
            
            for s in next_move:
                #if(s in self.KB.visited):
                if(self.KB.safe.count(s) > 0):
                    self.KB.visited.append(s)
                    while(self.KB.safe.count(s) > 0):
                        self.KB.safe.remove(s)
                    self.history_move = pos
                    res.append(s)
                    return res
            
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

            for s in next_move:
                if(self.KB.visited.count(s) > 0 and self.KB.stench.count(s) == 0 and self.KB.breeze.count(s) == 0):
                    res.append(s)
                    self.history_move = pos
                    return res

            res.append(self.history_move)
            self.history_move = pos
            return res
        
            
        