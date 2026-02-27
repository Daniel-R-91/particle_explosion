import pygame
from random import randint
import time

class App:
    def __init__(self):
        pygame.init()
        self.screen_height = 800
        self.screen_width = 1600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        icon = pygame.image.load("images/icon.png").convert_alpha()
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Particle explosion")
        self.sound = pygame.mixer.Sound("audio/sound.mp3")
        self.clock = pygame.time.Clock()
        self.running = True

        self.position = ()
        self.particles = []

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.sound.play()
                pos = pygame.mouse.get_pos()
                for _ in range(125):
                    self.particles.append(Particles(pos))

    def draw(self):
        self.screen.fill((0, 0, 0))

        for particle in self.particles:
            particle.update()
            particle.draw(self.screen)

        self.particles = [p for p in self.particles if p.alpha > 0]

    def run(self):
        while self.running:
            self.draw()
            self.handle_events()
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

class Particles:
    def __init__(self, position):
        self.position = position
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.velocity = (randint(-20, 20), randint(-20, 20))
        self.alpha = 255
        self.radius = 5

    def update(self):
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])
        self.alpha -= 5
        self.radius -= 0.2

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.position[0]), int(self.position[1])), self.radius)

if __name__ == "__main__":
    app = App()
    app.app_active = True
    app.run()

