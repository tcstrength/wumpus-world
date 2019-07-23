from entities.modelbox import ModelBox
from graphics.model import Model

class Stench(Model):
    def __init__(self):
        super().__init__("STENCH", ModelBox(0, 0, 64, 64))