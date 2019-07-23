from graphics.blank import Blank

class GameBoard:
    def __init__(self, row_count, col_count):
        self.board = list()
        for i in range(row_count):
            self.board.append(list())
            for j in range(col_count):
                self.board[i].append(None)

    def add_model(self, model, row, col):
        self.board[row][col] = model

    def draw(self, window):
        rows = len(self.board)
        cols = len(self.board[0])
        for i in range(rows):
            for j in range(cols):
                if (self.board[i][j] == None):
                    continue
                modelbox = self.board[i][j].modelbox
                modelbox.x = j * modelbox.width
                modelbox.y = (rows - i - 1) * modelbox.height
                self.board[i][j].modelbox = modelbox
                self.board[i][j].draw(window)
