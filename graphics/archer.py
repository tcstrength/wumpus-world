from graphics.model import Model
from entities.modelbox import ModelBox

class Archer(Model):
    def __init__(self):
        super().__init__("ARCHER", ModelBox(0, 0, 64, 64))