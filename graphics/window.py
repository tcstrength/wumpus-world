import pygame
from resources.images import Images
from entities.modelbox import ModelBox

class Window:
    def __init__(self, title, width = 800, height = 600):
        self.display = pygame.display
        self.display.set_caption(title)
        self.surface = self.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.images = Images()
        self.background = ""
        self.running = True

    def draw(self, path, modelbox):
        if (path == None or path == ""):
            return

        temp = pygame.transform.scale(self.images.get(path), (modelbox.width, modelbox.height))
        self.surface.blit(temp, (modelbox.x, modelbox.y))
    
    def begin(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

        self.surface.fill((255, 255, 255))
        self.draw(self.background, ModelBox(0, 0, 640, 640))

    def end(self):
        self.display.update()
        self.clock.tick(60)
