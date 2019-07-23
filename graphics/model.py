from entities import unittype

class Model:
    def __init__(self, typ, modelbox):
        self.type = typ
        self.image = unittype.IMAGES[self.type]
        self.modelbox = modelbox

    def draw(self, window):
        window.draw(self.image, self.modelbox)
        