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
    # --- Gulv ---
    pygame.draw.rect(screen, (160, 120, 80), (0, 600, 1100, 150)) #Gulv
    # --- Tavle ---
    pygame.draw.rect(screen, (100, 65, 35), (240, 330, 420, 180)) #Tavleramme
    pygame.draw.rect(screen, (40, 100, 70), (250, 340, 400, 160)) #Tavle
    # --- Vindu ---
    pygame.draw.rect(screen, (40, 70, 100), (700, 300, 280, 170)) #Vinduramme
    pygame.draw.rect(screen, (135, 205, 235), (710, 310, 260, 150)) #Vindu
    pygame.draw.rect(screen, (40, 70, 100), (837, 310, 6, 150)) # Streker i vinduet
    pygame.draw.rect(screen, (40, 70, 100), (710, 382, 260, 6)) # Streker i vinduet
    pygame.draw.rect(screen, (235, 235, 230), (690, 470, 300, 10)) #Vinduskarm
    # --- Klokke ---
    pygame.draw.circle(screen, (100, 65, 35), (450, 280), 35) #Klokkeramme
    pygame.draw.circle(screen, (250, 250, 245), (450, 280), 30) #Klokke
    pygame.draw.line(screen, (30, 30, 30), (450, 280), (450, 256),(2)) #Klokke minuttviser
    pygame.draw.line(screen, (30, 30, 30), (450, 280), (466, 280),(4)) #Klokke timeviser
    # --- Dør ---
    pygame.draw.rect(screen, (100, 65, 35), (60, 330, 140, 270)) #Dørkarm
    pygame.draw.rect(screen, (150, 105, 62), (70, 340, 120, 260)) #Dør
    pygame.draw.circle(screen, (210, 175, 70), (175, 460), (7)) #Dørhåndtak
    # --- Tak ---
    pygame.draw.rect(screen, (245, 245, 240), (0, 0, 1100, 200)) #Tak
    pygame.draw.rect(screen, (200, 200, 195), (0, 200, 1100, 10)) #Kant mellom tak og vegg
    # --- Lamper ---
    pygame.draw.rect(screen, (190, 190, 185), (100, 150, 180, 18)) #Ramme til lampe
    pygame.draw.rect(screen, (190, 190, 185), (460, 150, 180, 18)) #Ramme til lampe
    pygame.draw.rect(screen, (190, 190, 185), (820, 150, 180, 18)) #Ramme til lampe
    pygame.draw.rect(screen, (255, 255, 220), (105, 155, 170, 8)) #Lampe 
    pygame.draw.rect(screen, (255, 255, 220), (465, 155, 170, 8)) #Lampe
    pygame.draw.rect(screen, (255, 255, 220), (825, 155, 170, 8)) #Lampe
    # --- Røykvarsler ---
    pygame.draw.circle(screen, (230, 230, 225), (550, 60), (14)) #Røykvarsler stor runding
    pygame.draw.circle(screen, (120, 120, 120), (550, 60), (4)) #Røykvarler liten runding
    # --- Pult 1 ---
    pygame.draw.rect(screen, (120, 80, 40), (300, 580, 200, 15))    # Bordplate
    pygame.draw.rect(screen, (80, 80, 80), (320, 595, 12, 50))      # Bein venstre
    pygame.draw.rect(screen, (80, 80, 80), (476, 595, 12, 50))      # Bein høyre

    # --- Stolen til pult 1 ---
    pygame.draw.rect(screen, (100, 100, 100), (360, 610, 70, 12))   # Sete
    pygame.draw.rect(screen, (100, 100, 100), (360, 550, 12, 60))   # Stolrygg
    pygame.draw.rect(screen, (60, 60, 60), (370, 622, 8, 25))       # Stolbein venstre
    pygame.draw.rect(screen, (60, 60, 60), (412, 622, 8, 25))       # Stolbein høyre
    
    # --- Søppelbøtte ---
    pygame.draw.rect(screen, (80, 80, 80), (15, 575, 35, 45))     # Søppelbøtte
    pygame.draw.ellipse(screen, (110, 110, 110), (10, 570, 45, 12)) # Lokk til Søppelbøtte





    pygame.display.flip()
pygame.quit()