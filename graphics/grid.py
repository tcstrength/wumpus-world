from graphics.model import Model
from entities.modelbox import ModelBox

class Grid(Model):
    def __init__(self):
        super().__init__("GRID", ModelBox(0, 0, 640, 640))
    