from graphics.model import Model
from entities import unittype
from entities.modelbox import ModelBox

class Grid(Model):
    def __init__(self):
        super().__init__(unittype.GRID, ModelBox(0, 0, 640, 640))
    