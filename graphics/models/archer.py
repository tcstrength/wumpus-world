from graphics.model import Model
from entities.modelbox import ModelBox

class Archer(Model):
    
    
    def __init__(self):
        super().__init__("ARCHER", ModelBox(0, 0, 64, 64))
        self.current = ""
        self.score = 0
        
    def Pick_gold(BtnPos):
        if (BtnPos.Tag != None):
            if (BtnPos.Tag.ToString().Contains("glitter")):
                score += 100;
            
        

    '''def isDie():
        if (self._current.Tag != None):
            if (self._current.Contains("pit") or self._current.Contains("wumpus")):
                return True
        return False'''
        
        

    