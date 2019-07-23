from entities.modelbox import ModelBox
from graphics.model import Model

class Wumpus(Model):
    def __init__(self):
        super().__init__("WUMPUS", ModelBox(0, 0, 64, 64))