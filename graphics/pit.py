from entities.modelbox import ModelBox
from graphics.model import Model

class Pit(Model):
    def __init__(self):
        super().__init__("PIT", ModelBox(0, 0, 64, 64))