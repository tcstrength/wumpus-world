from resources.data import gamedata

class Model:
    def __init__(self, type, modelbox):
        self.type = gamedata.get_type(type)
        self.image = self.type["image"]
        self.modelbox = modelbox

    def set_point(self, point):
        self.modelbox.x = point[0]
        self.modelbox.y = point[1]

    def get_point(self):
        return [self.modelbox.x, self.modelbox.y]

    def get_size(self):
        return [self.modelbox.width, self.modelbox.height]

    def draw(self, window):
        window.draw(self.image, self.modelbox)
        