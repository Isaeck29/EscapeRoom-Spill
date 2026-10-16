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
    pygame.draw.rect(screen, (100, 65, 35), (240, 330, 420, 180)) #Tavleramme
    pygame.draw.rect(screen, (40, 100, 70), (250, 340, 400, 160)) #Tavle
    pygame.draw.rect(screen, (40, 70, 100), (700, 300, 280, 170)) #Vinduramme
    pygame.draw.rect(screen, (135, 205, 235), (710, 310, 260, 150)) #Vindu
    pygame.draw.rect(screen, (40, 70, 100), (837, 310, 6, 150)) # Streker i vinduet
    pygame.draw.rect(screen, (40, 70, 100), (710, 382, 260, 6)) # Streker i vinduet
    pygame.draw.rect(screen, (235, 235, 230), (690, 470, 300, 10)) #Vinduskarm
    pygame.draw.circle(screen, (100, 65, 35), (450, 280), 35) #Klokkeramme
    pygame.draw.circle(screen, (250, 250, 245), (450, 280), 30) #Klokke
    pygame.draw.line(screen, (30, 30, 30), (450, 280), (450, 256),(2)) #Klokke minuttviser
    pygame.draw.line(screen, (30, 30, 30), (450, 280), (466, 280),(4)) #Klokke timeviser
    pygame.draw.rect(screen, (100, 65, 35), (60, 330, 140, 270)) #Dørkarm
    pygame.draw.rect(screen, (150, 105, 62), (70, 340, 120, 260)) #Dør
    pygame.draw.circle(screen, (210, 175, 70), (175, 460), (7)) #Dørhåndtak
    pygame.draw.rect(screen, (245, 245, 240), (0, 0, 1100, 200)) #Tak
    pygame.draw.rect(screen, (200, 200, 195), (0, 200, 1100, 10)) #Kant mellom tak og vegg
    pygame.draw.rect(screen, (190, 190, 185), (100, 150, 180, 18)) #Ramme til lampe
    pygame.draw.rect(screen, (190, 190, 185), (460, 150, 180, 18)) #Ramme til lampe
    pygame.draw.rect(screen, (190, 190, 185), (820, 150, 180, 18)) #Ramme til lampe
    pygame.draw.rect(screen, (255, 255, 220), (105, 155, 170, 8)) #Lampe 
    pygame.draw.rect(screen, (255, 255, 220), (465, 155, 170, 8)) #Lampe
    pygame.draw.rect(screen, (255, 255, 220), (825, 155, 170, 8)) #Lampe
    pygame.draw.circle(screen, (230, 230, 225), (550, 60), (14)) #Røykvarsler stor runding
    pygame.draw.circle(screen, (120, 120, 120), (550, 60), (4)) #Røykvarler liten runding
    pygame.display.flip()
pygame.quit()