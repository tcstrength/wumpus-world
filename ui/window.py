import pygame

class Window:
    def __init__(self, title, width = 800, height = 600):
        self.display = pygame.display
        self.display.set_mode((width, height))
        self.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while (self.running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = True

            self.display.update()
            self.clock.tick(60)
