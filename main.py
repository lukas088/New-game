import pygame
pygame.init()

pygame.display.set_mode((600, 400), pygame.RESIZABLE)
pygame.display.set_caption("New Game")
pygame.display.set_icon(pygame.image.load("free-icon-gems-1037918.png"))

clock = pygame.time.Clock()
FPS = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(FPS)