import pygame

pygame.init()

WIDTH = 1100
HEIGHT = 750

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape Room - Klasserommet")

running = True

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((220, 230, 240))
    pygame.draw.rect(screen, (160, 120, 80), (0, 600, 1100, 150)) #Gulv
    pygame.draw.rect(screen, (100, 65, 35), (240, 150, 420, 180)) #Tavleramme
    pygame.draw.rect(screen, (40, 100, 70), (250, 160, 400, 160)) #Tavle
    pygame.draw.rect(screen, (40, 70, 100), (700, 190, 280, 170)) #Vinduramme
    pygame.draw.rect(screen, (135, 205, 235), (710, 200, 260, 150)) #Vindu
    pygame.draw.rect(screen, (40, 70, 100), (837, 200, 6, 150)) # Streker i vinduet
    pygame.draw.rect(screen, (40, 70, 100), (710, 272, 260, 6)) # Streker i vinduet
    pygame.draw.rect(screen, (235, 235, 230), (690, 360, 300, 10)) #Vinduskarm
    pygame.draw.circle(screen, (100, 65, 35), (450, 100), 35) #Klokkeramme
    pygame.draw.circle(screen, (250, 250, 245), (450, 100), 30) #Klokke
    pygame.draw.line(screen, (30, 30, 30), (450, 100), (450, 76),(2)) #Klokke minuttviser
    pygame.draw.line(screen, (30, 30, 30), (450, 100), (466, 100),(4)) #Klokke timeviser
    pygame.draw.rect(screen, (100, 65, 35), (60, 330, 140, 270)) #Dørkarm
    pygame.draw.rect(screen, (150, 105, 62), (70, 340, 120, 260)) #Dør
    pygame.draw.circle(screen, (210, 175, 70), (175, 460), (7)) #Dørhåndtak
    pygame.display.flip()
pygame.quit()