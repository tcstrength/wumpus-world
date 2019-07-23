from resources.data import gamedata

class Model:
    def __init__(self, type, modelbox):
        self.type = gamedata.get_type(type)
        self.image = self.type["image"]
        self.modelbox = modelbox

    def draw(self, window):
        window.draw(self.image, self.modelbox)
        