import pygame
from entities.modelbox import ModelBox
from graphics.model import Model
from entities import unittype

class Pit(Model):
    def __init__(self):
        super().__init__(unittype.PIT, ModelBox(0, 0, 64, 64))