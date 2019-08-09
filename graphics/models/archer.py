from graphics.model import Model
from entities.modelbox import ModelBox

class Archer(Model):
    _currentBtn = ""
    _score = 0
    
    def __init__(self):
        super().__init__("ARCHER", ModelBox(0, 0, 64, 64))
        
    def Start(button, image):
        _currentBtn = button
        '''
        button.Enabled = true
        button.BackgroundImage = image
        '''
        _score = 0
        
    def Move(dstBtn, image):
        '''
            dst.Enabled = true;
            current.BackgroundImage = null;
            dst.BackgroundImageLayout = ImageLayout.Stretch;
            dst.BackgroundImage = var;

            if (current.BackColor != Color.White && current.Tag is null)
                current.BackColor = Color.White;
            if (current.Tag != null && current.Tag.ToString().Contains("stench"))
            {
                current.BackColor = Color.Red;
            }

            if (current.Tag != null && current.Tag.ToString().Contains("breeze"))
            {
                current.BackColor = Color.Blue;
            }
            current.Enabled = false;
            current = dst;
        '''
        def Pick_gold(BtnPos):
            if (BtnPos.Tag != None):
                if (BtnPos.Tag.ToString().Contains("glitter")):
                    score += 100;
            
        

        def isDie():
            if (_currentBtn.Tag != None):
                if (_currentBtn.Tag.ToString().Contains("pit") or _currentBtn.Tag.ToString().Contains("wumpus")):
                    return True
            return False
        
        

    