import pygame

pygame.init()

WIDTH = 900
HEIGHT = 650

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape Room - Klasserommet")

running = True

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((220, 230, 240))
    pygame.draw.rect(screen, (160, 120, 80), (0, 500, 900, 150))
    pygame.draw.rect(screen, (100, 65, 35), (240, 90, 420, 220))
    pygame.draw.rect(screen, (40, 100, 70), (250, 100, 400, 200))
    pygame.display.flip()
pygame.quit()
