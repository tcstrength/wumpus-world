from graphics.models.grid import Grid
from graphics.models.breeze import Breeze
from graphics.models.stench import Stench
from resources.data import gamedata

class GameBoard:
    def __init__(self, row_count, col_count):
        self.breeze_model = Breeze()
        self.stench_model = Stench()
        self.model_table = []
        self.stench_table = []
        self.breeze_table = []
        self.grid = Grid()
        for i in range(row_count):
            self.model_table.append([])
            self.stench_table.append([])
            self.breeze_table.append([])
            for j in range(col_count):
                self.model_table[i].append(None)
                self.stench_table[i].append(False)
                self.breeze_table[i].append(False)

    def is_legal(self, row, col):
        row_count = len(self.model_table)
        col_count = len(self.model_table[0])
        return row >= 0 and col >= 0 and row < row_count and col < col_count

    def add_breeze(self, row, col):
        rows = [row - 1, row    ,row + 1, row]
        cols = [col    , col - 1, col   , col + 1]
        for i in range(4):
            if (self.is_legal(rows[i], cols[i])):
                self.breeze_table[rows[i]][cols[i]] = True

    def add_stench(self, row, col):
        rows = [row - 1, row    ,row + 1, row]
        cols = [col    , col - 1, col   , col + 1]

        for i in range(4):
            if (self.is_legal(rows[i], cols[i])):
                self.stench_table[rows[i]][cols[i]] = True

    def add_model(self, model, row, col):
        self.model_table[row][col] = model
        if (model.type == gamedata.get_type("PIT")):
            self.add_breeze(row, col)
        elif (model.type == gamedata.get_type("WUMPUS")):
            self.add_stench(row, col)

    def draw_model(self, window, model, row, col):
        if (model == None):
            return

        modelbox = model.modelbox
        modelbox.x = col * modelbox.width
        modelbox.y = row * modelbox.height
        model.modelbox = modelbox
        model.draw(window)

    def draw_breeze(self, window, row, col):
        if (self.breeze_table[row][col] == False):
            return
        self.draw_model(window, self.breeze_model, row, col)

    def draw_stench(self, window, row, col):
        if (self.stench_table[row][col] == False):
            return
        self.draw_model(window, self.stench_model, row, col)

    def draw(self, window):
        row_count = len(self.model_table)
        col_count = len(self.model_table[0])

        for i in range(row_count):
            for j in range(col_count):
                self.draw_model(window, self.model_table[i][j], i, j)
                self.draw_breeze(window, i, j)
                self.draw_stench(window, i, j)

        self.grid.draw(window)
