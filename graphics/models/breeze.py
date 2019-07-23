from entities.modelbox import ModelBox
from graphics.model import Model

class Breeze(Model):
    def __init__(self):
        super().__init__("BREEZE", ModelBox(0, 0, 64, 64))