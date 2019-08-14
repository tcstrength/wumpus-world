
class KB:
    def __init__(self):
        self.unknown = []
        self.pit = []
        self.wumpus = []
        self.stench = []
        self.breeze = []
        self.visited = []
        self.safe = []
        
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
            if(self.pit.count(s) == 0 or self.wumpus.count(s) == 0):
                arrMove.append(s)
        if(x + 1 <= 9):
            posX = x + 1
            posY = y 
            s = chr(posY + 48) + ',' + chr(posX + 48)
            if(self.pit.count(s) == 0 or self.wumpus.count(s) == 0):
                arrMove.append(s)
        if(y - 1 >= 0):
            posX = x
            posY = y - 1 
            s = chr(posY + 48) + ',' + chr(posX + 48)
            if(self.pit.count(s) == 0 or self.wumpus.count(s) == 0):
                arrMove.append(s)
        if(y + 1 <= 9):
            posX = x
            posY = y + 1
            s =  chr(posY + 48) + ',' + chr(posX + 48)
            if(self.pit.count(s) == 0 or self.wumpus.count(s) == 0):
                arrMove.append(s)
        
        return arrMove
    
    def addStench(self, str):
        self.stench.append(str)
        moves = self.PossibleMove(str)
        for move in moves:
            if(self.safe.count(move) > 0 or self.visited.count(move) > 0):
                moves.remove(move)
                continue
            else:
                self.infereWumpus(move)
        
    def addBreeze(self, str):
        self.breeze.append(str)
        moves = self.PossibleMove(str)
        for move in moves:
            if(self.safe.count(move) > 0 or self.visited.count(move) > 0):
                moves.remove(move)
                continue
            else:
                self.inferePit(move)
        
    def addSafe(self, str):
        self.safe.append(str)
            
    def inferePit(self, str):
        if(self.pit.count(str) > 0):
            return;
        count = 0
        moves = self.PossibleMove(str)
        for move in moves:
            if(self.visited.count(move) > 0 and self.breeze.count(move) == 0):
                return
            else:
                if(self.breeze.count(move) > 0 and self.safe.count(move) == 0):
                    count = count + 1
                
        if(count >= 2 and self.pit.count(str) == 0):
            self.pit.append(str)
            if(self.unknown.count(str)):
                self.unknown.remove(str)
            for move in moves:
                if(self.unknown.count(move) > 0):
                    self.unknown.remove(move)
        else:
            self.unknown.append(str)
            
    def infereWumpus(self, str):
        if(self.wumpus.count(str) > 0):
            return;
        count = 0
        moves = self.PossibleMove(str)
        for move in moves:
            if(self.visited.count(move) > 0 and self.breeze.count(move) == 0):
                return
            else:
                if(self.stench.count(move) and self.safe.count(move) == 0):
                    count = count + 1
                
        if(count >= 2 and self.wumpus.count(str) == 0):
            self.wumpus.append(str)
            if(self.unknown.count(str)):
                self.unknown.remove(str)
            for move in moves:
                if(self.unknown.count(move) > 0):
                    self.unknown.remove(move)
        else:
            self.unknown.append(str)
            
            
        