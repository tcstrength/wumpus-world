
class KB:
    def __init__(self):
        self.pit = []
        self.wumpus = []
        self.stench = []
        self.breeze = []
        self.visited = []
        self.safe = []
        
    def addStench(self, str):
        self.stench.append(str)
        self.infereWumpus()
        
    def addBreeze(self, str):
        self.breeze.append(str)
        self.inferePit()
        
    def addSafe(self, str):
        self.safe.append(str)
            
    def inferePit(self):
        for pos in self.breeze:
            temp = pos.split(',')
            y = int(temp[0])
            x = int(temp[1])
            
            diagnose = []
            temp1 = ""
            # Down Right Diag
            if(x + 1 <= 9 and y + 1 <= 9):
                temp1 = chr(y + 1 + 48) + ',' + chr(x + 1 + 48)
                if(self.breeze.count(temp1) == 0):
                    if(self.visited.count(temp1) > 0 or self.safe.count(temp1) > 0):
                        local = chr(y - 1 + 48) + ',' + chr(x + 1 + 48)
                        if(self.safe.count(local) == 0):
                            self.safe.append(local)
                        local = chr(y + 1 + 48) + ',' + chr(x - 1 + 48)
                        if(self.safe.count(local) == 0):
                            self.safe.append(local)
                            
            # Up Right Diag
            if(x - 1 >= 9 and y + 1 <= 9):
                temp1 = chr(y + 1 + 48) + ',' + chr(x - 1 + 48)
                if(self.breeze.count(temp1) == 0):
                    if(self.visited.count(temp1) > 0 or self.safe.count(temp1) > 0):
                        local = chr(y + 48) + ',' + chr(x - 1 + 48)
                        if(self.safe.count(local) == 0):
                            self.safe.append(local)
                        local = chr(y + 48) + ',' + chr(x - 1 + 48)
                        if(self.safe.count(local) == 0):
                            self.safe.append(local)
                            
            # Up Left Diag
            if(x - 1 >= 0 and y - 1 >= 0):
                temp1 = chr(y - 1 + 48) + ',' + chr(x - 1 + 48)
                if(self.breeze.count(temp1) == 0):
                    if(self.visited.count(temp1) > 0 or self.safe.count(temp1) > 0):
                        local = chr(y - 1 + 48) + ',' + chr(x + 48)
                        if(self.safe.count(local) == 0):
                            self.safe.append(local)
                        local = chr(y + 48) + ',' + chr(x - 1 + 48)
                        if(self.safe.count(local) == 0):
                            self.safe.append(local)
            
            # Down Left Diag
            if(x + 1 <= 9 and y - 1 >= 0):
                temp1 = chr(y - 1 + 48) + ',' + chr(x + 1 + 48)
                if(self.breeze.count(temp1) == 0):
                    if(self.visited.count(temp1) > 0 or self.safe.count(temp1) > 0):
                        local = chr(y - 1 + 48) + ',' + chr(x + 48)
                        if(self.safe.count(local) == 0):
                            self.safe.append(local)
                        local = chr(y + 48) + ',' + chr(x + 1 + 48)
                        if(self.safe.count(local) == 0):
                            self.safe.append(local)
            

                            
    def infereWumpus(self):
        for pos in self.stench:
            temp = pos.split(',')
            y = int(temp[0])
            x = int(temp[1])
            
            diagnose = []
            temp1 = ""
            # Down Right Diag
            if(x + 1 <= 9 and y + 1 <= 9):
                temp1 = chr(y + 1 + 48) + ',' + chr(x + 1 + 48)
                if(self.stench.count(temp1) == 0):
                    if(self.visited.count(temp1) > 0 or self.safe.count(temp1) > 0):
                        local = chr(y - 1 + 48) + ',' + chr(x + 1 + 48)
                        if(self.safe.count(local) == 0):
                            self.safe.append(local)
                        local = chr(y + 1 + 48) + ',' + chr(x - 1 + 48)
                        if(self.safe.count(local) == 0):
                            self.safe.append(local)
                            
            # Up Right Diag
            if(x - 1 >= 0 and y + 1 <= 9):
                temp1 = chr(y + 1 + 48) + ',' + chr(x - 1 + 48)
                if(self.stench.count(temp1) == 0):
                    if(self.visited.count(temp1) > 0 or self.safe.count(temp1) > 0):
                        local = chr(y + 48) + ',' + chr(x - 1 + 48)
                        if(self.safe.count(local) == 0):
                            self.safe.append(local)
                        local = chr(y + 48) + ',' + chr(x - 1 + 48)
                        if(self.safe.count(local) == 0):
                            self.safe.append(local)
                            
            # Up Left Diag
            if(x - 1 >= 0 and y - 1 >= 0):
                temp1 = chr(y - 1 + 48) + ',' + chr(x - 1 + 48)
                if(self.stench.count(temp1) == 0):
                    if(self.visited.count(temp1) > 0 or self.safe.count(temp1) > 0):
                        local = chr(y - 1 + 48) + ',' + chr(x + 48)
                        if(self.safe.count(local) == 0):
                            self.safe.append(local)
                        local = chr(y + 48) + ',' + chr(x - 1 + 48)
                        if(self.safe.count(local) == 0):
                            self.safe.append(local)
            
            # Down Left Diag
            if(x + 1 <= 9 and y - 1 >= 0):
                temp1 = chr(y - 1 + 48) + ',' + chr(x + 1 + 48)
                if(self.stench.count(temp1) == 0):
                    if(self.visited.count(temp1) > 0 or self.safe.count(temp1) > 0):
                        local = chr(y - 1 + 48) + ',' + chr(x + 48)
                        if(self.safe.count(local) == 0):
                            self.safe.append(local)
                        local = chr(y + 48) + ',' + chr(x + 1 + 48)
                        if(self.safe.count(local) == 0):
                            self.safe.append(local)
            
        