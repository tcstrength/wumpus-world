from graphics.models.grid import Grid
from graphics.models.breeze import Breeze
from graphics.models.stench import Stench
from graphics.models.pit import Pit
from graphics.models.wumpus import Wumpus
from graphics.models.archer import Archer
from graphics.models.gold import Gold
from graphics.models.blank import Blank
from resources.data import gamedata
from entities.types import *

class GameBoard:
    def __init__(self, map):
        self.map = map
        self.grid_model = Grid()
        self.blank_model = Blank()
        self.game_models = {
            AGENT: Archer(),
            PIT: Pit(),
            GOLD: Gold(),
            WUMPUS: Wumpus(),
            BREEZE: Breeze(),
            STENCH: Stench()
        }

    def draw_model(self, window, model, r, c):
        size = model.get_size()
        point = model.get_point()
        point[0] = c * size[0]
        point[1] = r * size[1]
        model.set_point(point)
        model.draw(window)
    
    def draw_models(self, window, r, c):
        for key in self.game_models.keys():
            if (self.map.has_status(r, c, key)):
                self.draw_model(window, self.game_models[key], r, c)

    def draw(self, window):
        row_count = self.map.get_row_count()
        col_count = self.map.get_col_count()
        for r in range(row_count):
            for c in range(col_count):
                if (self.map.cell_table[r][c].closed):
                    self.draw_model(window, self.blank_model, r, c)
                else:
                    self.draw_models(window, r, c)

        self.grid_model.draw(window)
        