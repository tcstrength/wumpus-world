from graphics.model import Model
from entities.modelbox import ModelBox

class Gold(Model):
    def __init__(self):
        super().__init__("GOLD", ModelBox(0, 0, 64, 64))