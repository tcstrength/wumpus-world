from graphics.model import Model
from entities import unittype
from entities.modelbox import ModelBox

class Blank(Model):
    def __init__(self):
        super().__init__(unittype.BLANK, ModelBox(0, 0, 64, 64))