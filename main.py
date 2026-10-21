import pygame

pygame.init()
pygame.font.init() # Starter font-systemet slik at tekst kan vises på skjermen

# Skrifttype med font og størrelse. Denne bruker standardfont i pygame
skrift = pygame.font.SysFont(None, 28)

WIDTH = 1100
HEIGHT = 750

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape Room - Klasserommet")

running = True

# Variabler for gjenstander som kan plukkes opp
potet_plukket = False
lapp_plukket = False

# Inventar-variabler
inventar = []       # Liste over ting man har samlet opp
inventar_apen = False # Passer på om inventaret vises på skjermen eller ikke

while running == True:
    # ============================================
    #   HÅNDTERER ULIKE INPUTS FRA BRUKEREN
    # ============================================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Henter posisjonen til musepekeren når det klikkes
            mus_x, mus_y = pygame.mouse.get_pos()
            
            # Sjekker klikk inni inventaret (hvis det er åpent)
            if inventar_apen:
                if "Sammenkrøllet Lapp" in inventar:
                    lapp_indeks = inventar.index("Sammenkrøllet Lapp") #Sjekker hvilken plass i inventaret lappen har. 
                    lapp_y = 280 + (lapp_indeks * 40) 
                    lapp_i_inventar_boks = pygame.Rect(390, lapp_y, 250, 30) #Legger klikboksen til lappen på riktig sted i inventaret

                    #Sjekker om musepekeren klikker inne i boksen til lappen i inventaret
                    if lapp_i_inventar_boks.collidepoint(mus_x, mus_y):
                        print("Du brettet ut lappen fra inventaret:")
                        print("På lappen står det: 'Koderekkefølge: Klokke -> Bøker -> Tavle -> Skuff'")
            
            else:
                # Klikkboksen til poteten
                potet_boks = pygame.Rect(1014, 555, 38, 26)
                if potet_boks.collidepoint(mus_x, mus_y) and not potet_plukket:
                    potet_plukket = True
                    inventar.append("Potet") # Legger poteten inn i inventaret
                    print("Du plukket opp poteten, og la den i inventaret. Du vet ikke helt hva du skal bruke den til...")
                
                # Klikkboksen til søppelbøtta
                soppel_boks = pygame.Rect(10, 570, 45, 50)
                if soppel_boks.collidepoint(mus_x, mus_y) and not lapp_plukket:
                    lapp_plukket = True
                    inventar.append("Sammenkrøllet Lapp") #Legger lappen inn i inventaret
                    print("Du fant en sammenkrøllet lapp i søppelbøtta! Åpne inventaret ved å trykke 'i' og klikk på lappen for å lese den.")

                # Klikkboksen til tavla
                tavle_boks = pygame.Rect(250, 340, 400, 160)
                if tavle_boks.collidepoint(mus_x, mus_y):
                    print("På tavla står det skrevet med kritt: 'Bøker - Klokkeslett = ?'")

        # Sjekker om spilleren har trykket på en tast
        elif event.type == pygame.KEYDOWN:
            # Sjekker om spilleren har trykket på 'i'-tasten
            if event.key == pygame.K_i:
                # Bytter mellom true og false. Det åpner og lukker inventaret
                inventar_apen = not inventar_apen
    
    
    
    # ============================================
    # TEGNER OPP TING I KLASSEROMMET
    # ============================================
    screen.fill((220, 230, 240))
    # --- Gulv ---
    pygame.draw.rect(screen, (160, 120, 80), (0, 600, 1100, 150)) #Gulv
    
    # --- Tavle ---
    pygame.draw.rect(screen, (100, 65, 35), (240, 330, 420, 180)) #Tavleramme
    pygame.draw.rect(screen, (40, 100, 70), (250, 340, 400, 160)) #Tavle
    # Tekst skrevet på tavla med "kritt" (hvit farge)
    tavle_tekst = skrift.render("Bøker - Klokkeslett = ?", True, (240, 240, 240))
    screen.blit(tavle_tekst, (330, 400))

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

    # --- Bokhylle ---
    pygame.draw.rect(screen, (110, 70, 30), (980, 420, 100, 180))   # Bokhylle ramme
    pygame.draw.rect(screen, (90, 50, 20), (990, 430, 80, 160))    # Bokhylle innside
    pygame.draw.rect(screen, (110, 70, 30), (990, 480, 80, 6))    # Øverste hylle i bokhyllen
    pygame.draw.rect(screen, (110, 70, 30), (990, 535, 80, 6))    # Midterste hylle i bokhyllen
    pygame.draw.rect(screen, (110, 70, 30), (990, 590, 80, 10))   # Nederste hylle i bokhyllen
    
    # --- Bøker i hyllene ---
    pygame.draw.rect(screen, (200, 50, 50), (995, 445, 10, 35))     # Rød bok i øverste hylle
    pygame.draw.rect(screen, (50, 100, 200), (1008, 440, 12, 40))   # Blå bok i øverste hylle
    pygame.draw.rect(screen, (200, 200, 50), (1023, 448, 10, 32))   # Gul bok i øverste hylle
    pygame.draw.rect(screen, (150, 50, 150), (1036, 442, 12, 38))   # Lilla bok i øverste hylle
    pygame.draw.rect(screen, (40, 150, 90), (995, 500, 12, 35))     # Grønn bok i midterste hylle
    pygame.draw.rect(screen, (220, 120, 40), (1010, 495, 10, 40))   # Oransje bok i midterste hylle
    pygame.draw.rect(screen, (50, 50, 50), (1023, 502, 14, 33))     # Svart bok i midterste hylle
    
    # --- Potet (Om poteten er plukket opp vil ikke poteten tegnes) ---
    if not potet_plukket:
        pygame.draw.ellipse(screen, (110, 85, 55), (1014, 555, 38, 26)) #Potetens form
        pygame.draw.circle(screen, (55, 40, 25), (1022, 562), 2) #Potetdetaljer
        pygame.draw.circle(screen, (55, 40, 25), (1034, 568), 2) #potetdetaljer
        pygame.draw.circle(screen, (55, 40, 25), (1041, 560), 2) #Potetdetaljer
        pygame.draw.circle(screen, (55, 40, 25), (1026, 571), 1) #Potetdetaljer
        pygame.draw.circle(screen, (55, 40, 25), (1035, 562), 1) #Potetdetaljer
        pygame.draw.circle(screen, (55, 40, 25), (1021, 568), 1) #Potetdetaljer

    # --- INVENTAR-VINDUET (denne vil kun vises om inventar_apen er True) ---
    if inventar_apen:
        # Tegner en boks midt på skjermen
        pygame.draw.rect(screen, (60, 45, 30), (350, 200, 400, 300))     # Bokserammen
        pygame.draw.rect(screen, (240, 230, 210), (360, 210, 380, 280))   # Innsiden av boksen
        
        # Overskriften i inventaret
        tittel_bilde = skrift.render("INVENTAR", True, (40, 30, 20))
        screen.blit(tittel_bilde, (505, 225))
        
        # Går igjennom alt som ligger i inventar-listen og skriver det ut på skjermen
        start_y = 280
        for gjenstand in inventar:
            # Gjør teksten om til et bilde
            gjenstand_bilde = skrift.render("- " + gjenstand, True, (20, 20, 20))
            # Tegner teksten på skjermen
            screen.blit(gjenstand_bilde, (400, start_y))
            start_y += 40 # Flytter neste linje nedover hvis det er flere ting som skal i inventaret. 

    pygame.display.flip()

pygame.quit()