from entities.statustypes import *

class Cell:
    def __init__(self):
        self.status = 0
        self.closed = True

class GameMap:
    def __init__(self, row_count, col_count):
        self.Visited = []
        self.Safe = []
        self.cell_table = [[]] * row_count
        for i in range(row_count):
            self.cell_table[i] = [None] * col_count
            for j in range(col_count):
                self.cell_table[i][j] = Cell()

    # Return (row, col)
    def find_agent(self):
        for i in range(self.get_row_count()):
            for j in range(self.get_col_count()):
                if (self.has_status(i, j, AGENT)):
                    return [i, j]
        return [-1, -1]

    def findSafe(self):
        res = []
        for i in range(self.get_row_count()):
            for j in range(self.get_col_count()):
                if (self.has_status(i, j, WUMPUS) == False or self.has_status(i, j, PIT) == False):
                    res.append(chr(i + 48) + ',' + chr(j + 48))
        return res
    
    def load_map(self, path):
        f = open(path, "r")
        lines = f.read().splitlines()
        for i in range(len(lines)):
            chars = lines[i].split(" ")
            for j in range(len(chars)):
                if (chars[j] == "W"):
                    self.add_wumpus(i, j)
                elif (chars[j] == "P"):
                    self.add_pit(i, j)
                elif (chars[j] == "A"):
                    self.add_status(i, j, AGENT)
                    self.open(i, j)
                elif (chars[j] == "G"):
                    self.add_status(i, j, GOLD)

    def get_row_count(self):
        return len(self.cell_table)

    def get_col_count(self):
        return len(self.cell_table[0])

    def show_nude(self):
        for i in range(self.get_row_count()):
            line = ""
            for j in range(self.get_col_count()):
                line += str(self.cell_table[i][j].status) + " "
            print(line)

    def is_legal(self, row, col):
        zero = row >= 0 and col >= 0
        size = row < self.get_row_count() and col < self.get_col_count()
        return zero and size

    def __add_status_arround(self, row, col, status):
        rows = [row - 1, row    ,row + 1, row]
        cols = [col    , col - 1, col   , col + 1]
        for i in range(4):
            if (self.is_legal(rows[i], cols[i]) == False):
                continue
            self.add_status(rows[i], cols[i], status)

    def open(self, row, col):
        if (self.is_legal(row, col) == False):
            return
        self.cell_table[row][col].closed = False
        s = chr(row + 48) + ',' + chr(col + 48)
        self.Visited.append(s)
        self.Safe.append(s)

    def add_status(self, row, col, status):
        if (self.is_legal(row, col) == False):
            return
        self.cell_table[row][col].status |= status

    def del_status(self, row, col, status):
        if (self.is_legal(row, col) == False):
            return
        self.cell_table[row][col].status &= ~status

    def add_wumpus(self, row, col):
        self.add_status(row, col, WUMPUS)
        self.__add_status_arround(row, col, STENCH)

    def add_pit(self, row, col):
        self.add_status(row, col, PIT)
        self.__add_status_arround(row, col, BREEZE)

    def has_status(self, row, col, status):
        if (self.is_legal(row, col) == False):
            return False
        return (self.cell_table[row][col].status & status) > 0