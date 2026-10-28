import pygame
import time
pygame.init()
pygame.font.init() # Starter font-systemet slik at tekst kan vises på skjermen

# Skrifttype med font og størrelse. Denne bruker standardfont i pygame
skrift = pygame.font.SysFont(None, 28)

WIDTH = 1100
HEIGHT = 750

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape Room - Klasserommet")

# --- LASTER INN BILDET FOR VINDUET ---
try: # får programmet til å prøve å laste bildet
    tree_bilde = pygame.image.load("tree.gif")
    tree_bilde = pygame.transform.scale(tree_bilde, (600, 450))
except: # Gjør at programmet ikke kræsjer selv hvis bildet mangler, eller ikke vil laste. 
    tree_bilde = None 

running = True

# Variabler for gjenstander og elementer som kan endre seg
potet_plukket = False #Holder styr på om spilleren har plukket opp poteten enda.
lapp_plukket = False #holder styr på om spilleren har plukket opp lappen enda
skuff_apnet = False # Holder styr på om skuffen er åpnet eller lukket
skap_apnet = False # holder styr på om skapet er åpnet
kode2469_brukt = False # Holder styr på om koden "2469" er blitt brukt
vindu_apnet = False # Holder styr på om bilde-vinduet er åpent akkurat nå

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
            
            # Sjekker klikkene inni inventaret (hvis det er åpent)
            if inventar_apen:
                if "Sammenkrøllet Lapp" in inventar:
                    lapp_indeks = inventar.index("Sammenkrøllet Lapp") # Sjekker hvilken plass i inventaret lappen har. 
                    lapp_y = 280 + (lapp_indeks * 40) # Regner ut y-posisjonen til lappen i inventaret basert på hvilken plass den har i listen
                    lapp_i_inventar_boks = pygame.Rect(390, lapp_y, 250, 30) # Legger klikkboksen til lappen på riktig sted i inventaret
                    
                    # Sjekker om musepekeren klikker inne i boksen til lappen i inventaret
                    if lapp_i_inventar_boks.collidepoint(mus_x, mus_y):
                        print("Du brettet ut lappen fra inventaret:")
                        print("På lappen står det: 'Koderekkefølge: Klokke -> Bøker -> Tavle -> Skuff'")
            
            else:
                # Klikkboksen til poteten
                potet_boks = pygame.Rect(1014, 555, 38, 26)
                if potet_boks.collidepoint(mus_x, mus_y) and not potet_plukket: # Sjekker at poteten ikke allerede er plukket opp
                    potet_plukket = True
                    inventar.append("Potet") # Legger poteten inn i inventaret
                    print("Du plukket opp poteten, og la den i inventaret. Du vet ikke helt hva du skal bruke den til...")
                
                # Klikkboksen til søppelbøtta
                soppel_botte = pygame.Rect(10, 570, 45, 50)
                if soppel_botte.collidepoint(mus_x, mus_y) and not lapp_plukket: # Sjekker at lappen ikke allerede er plukket opp
                    lapp_plukket = True
                    inventar.append("Sammenkrøllet Lapp") # Legger lappen inn i inventaret
                    print("Du fant en sammenkrøllet lapp i søppelbøtta! Åpne inventaret ved å trykke 'i' og klikk på lappen for å lese den.")

                # Klikkboksen til tavla
                tavle_boks = pygame.Rect(250, 340, 400, 160)
                if tavle_boks.collidepoint(mus_x, mus_y):
                    print("På tavla står det skrevet med kritt: 'Bøker - Klokkeslett = ?'")

                # Klikkboksen til vinduet (åpner/lukker tre-bildet/gif-en)
                vindu_boks = pygame.Rect(700, 300, 280, 170)
                if vindu_boks.collidepoint(mus_x, mus_y):
                    vindu_apnet = not vindu_apnet
                    if vindu_apnet:
                        print("Du ser ut av vinduet.")
                    else:
                        print("Du gikk bort fra vinduet.")

                # Klikkboksen til den øverste skuffen
                skuff_boks = pygame.Rect(860, 490, 90, 38)
                if skuff_boks.collidepoint(mus_x, mus_y):
                    skuff_apnet = not skuff_apnet # Bytter mellom true og false. Det åpner og lukker skuffen fordi "not" endrer verdien til det motsatte av det det var før.
                    if skuff_apnet:
                        print("Du dro opp skuffen. Inni er det risset inn et tall: 9")
                    else:
                        print("Du lukket skuffen igjen.")

                # Klikkboksen til det nederste skapet
                skap_boks = pygame.Rect(860, 535, 90, 55)
                if skap_boks.collidepoint(mus_x, mus_y):
                    skap_apnet = not skap_apnet # Bytter mellom true og false. Åpner og lukker skapet
                    if skap_apnet:
                        print("Du åpnet skapdøren. Skapet er helt tomt, bortsett fra et lite ':3' som er tegnet på bakveggen.")
                    else:
                        print("Du lukket igjen skapdøren.")

                # Klikkboksen til røykvarsleren
                roykvarsler_boks = pygame.Rect(536, 46, 28, 28)
                if roykvarsler_boks.collidepoint(mus_x, mus_y):
                    print("En helt vanlig røykvarsler. Den henger stille og rolig i taket og passer på")

                # Klikkboksen til klokka
                klokke_boks = pygame.Rect(415, 245, 70, 70)
                if klokke_boks.collidepoint(mus_x, mus_y):
                    print("Klokken på veggen viser hvit timeviser på 12 og minuttviser på 3. Klokken er 3!")

                # Klikkboksen til døra (Kodelåsen)
                dor_boks = pygame.Rect(60, 330, 140, 270)
                if dor_boks.collidepoint(mus_x, mus_y):
                    print("Du prøver å åpne døren, men den er låst med en kodelås.")
                    skrevet_kode = input("Skriv inn 4-sifret kode i terminalen: ")
                    
                    if skrevet_kode == "3749":
                        print("Du skrev riktig kode! Låsen klikker grønt, og døren glir opp. DU VANT SPILLET!")
                        running = False # Lukker spillet når spilleren vinner
                    elif skrevet_kode == "6767":
                        print("Er du dum? 6767 gir jo ingen mening, skjerp deg!")
                    elif skrevet_kode == "1234":
                        print("Beklager, men koden er ikke så enkel dessverre.")
                    elif skrevet_kode == "6969":
                        print("Hehe, du prøvde å være morsom ved å skrive koden 6969, men det funket ikke.")
                    elif skrevet_kode == "5505": #Easteregg ettersom det var en kode jeg fikk fra Jasper.
                        print("Er du Jasper?")
                        svar = input("Ja/Nei:").lower() #.lower får alt det som blir skrevet som input til å bli små bokstaver.
                        if svar == "ja":
                            print("Hei Jasper!")
                        elif svar == "nei": 
                            print("Nei, du er ikke Jasper. Men det er greit, Jasper er en rar fyr.") #Jasper er en rar fyr, men det er ikke negativt.
                        elif svar == "ost":
                            print("Ost? Hva mener du med det? Du må være Jasper!")
                        else:
                            print("Jeg forstår ikke svaret ditt :(")
                    elif skrevet_kode == "9717":    # Easteregg for Emil sin kode. 
                        print (":3")
                    elif skrevet_kode == "2469": # Easteregg med koden jeg fikk fra Åsmund
                        if not kode2469_brukt: # Sjekker om koden allerede har blitt brukt
                            kode2469_brukt = True # Gjør at spillkoden vet at denne koden allerede er brukt.  
                            print("Well, there is a man here. ") # Tekst fra spillet til Åsmund
                            time.sleep(1.2) # Får koden til å vente i 1,2 sekunder før den printer neste linje.
                            print("He offered you something...  ") # Tekst fra spillet til Åsmund
                            time.sleep(1.2) # Får koden til å vente i 1,2 sekunder før den printer neste linje.
                            svar = input("Accept the offer? Yes/No: ").lower() # Tekst fra spillet til Åsmund
                            if svar == "yes":
                                print("There is not a man here. ")  # Står på engelsk for å matche språket på spillet til Åsmund
                            elif svar == "no": 
                                print ("There was no man here, but you still feel guilty for not accepting the offer... ")  # Står på engelsk for å matche språket på spillet til Åsmund
                            elif svar == "proceed":
                                svar = input ("Proceed? Try writing Yes or No instead: ").lower()         
                                if svar == "proceed":
                                    svar = input ("Proceed?!?! Try writing Yes or No instead!: ").lower()
                                    if svar == "proceed":
                                        svar = input ("Why are you typing proceed! Try writing Yes or No instead!: ").lower()
                                        if svar == "proceed":
                                            svar = input ("STOP WRITING PROCEED!!!: ").lower()
                                            if svar == "proceed":
                                                svar = input ("Proceed? Try writing Yes or No instead: ").lower()
                                                if svar == "proceed":
                                                    svar = input ("OK, it was worth a shot trying to fake a loop. Please stop writing proceed: ").lower()
                                                    if svar == "proceed":
                                                        svar = input ("Trust me, you do not want to keep on writing proceed... ").lower()
                                                        if svar == "proceed":
                                                            svar = input ("STOP IT, YOU CAN'T KEEP ON DOING THIS! ").lower()
                                                            if svar == "proceed":
                                                                print ("Last chance... ")
                                                                time.sleep(1.0)
                                                                svar = input ("I am not kidding... ").lower()
                                                                if svar == "proceed":
                                                                    print ("Sorry, i was not joking at all... ")
                                                                    time.sleep(1.0)
                                                                    print ("Your game will end itself in 5 seconds... ")
                                                                    time.sleep (1.0)
                                                                    print ("5 ")
                                                                    time.sleep(1.0)
                                                                    print ("4 ")
                                                                    time.sleep(1.0)
                                                                    print ("3 ")
                                                                    time.sleep(1.0)
                                                                    print ("2 ")
                                                                    time.sleep(1.0)
                                                                    print ("1 ")
                                                                    time.sleep(1.0)
                                                                    print ("0 ")
                                                                    time.sleep(1.0)
                                                                    print ("...")
                                                                    time.sleep(1.0)
                                                                    print ("...")
                                                                    time.sleep(1.0)
                                                                    print ("We identified a problem while executing this command... ")
                                                                    time.sleep(1.0)
                                                                    print ("...")
                                                                    time.sleep(0.5)
                                                                    print ("WHAT?!? ")
                                                                    time.sleep(1.0)
                                                                    print ("It didn't work?!?! ")
                                                                    time.sleep(1.0)
                                                                    print ("ok forget i was here... ")
                                                                    time.sleep (3.0)
                                                                    print ("Well, there is a man here. ")
                                                                    time.sleep (1.0)
                                                                    print ("He offered you something... ")
                                                                    time.sleep (1.0)
                                                                    svar = input ("Accept the offer? Yes/No: ").lower()
                                                                    if svar == "Proceed" or svar == "proceed":
                                                                        print ("You have exceeded your limit of Proceed uses")
                                                                        time.sleep (1.0)
                                                                        print ("Try again later")
                                                                    else:
                                                                        print ("There is not a man here.")

                                                                else: 
                                                                    print ("You stopped saying proceed just in time...")
                                                                    time.sleep(1.0)
                                                                    print ("There was never a man here...")
                                                            else: 
                                                                print ("There is not a man here.")
                                                        else:
                                                            print ("There is not a man here.")
                                                    else:
                                                        print ("There is not a man here.")
                                                else:
                                                    print ("There is not a man here.")
                                            else:
                                                print ("There is not a man here.")
                                        else:
                                            print ("There is not a man here.")
                                    else:
                                        print ("There is not a man here.")
                                else:
                                    print ("There is not a man here.")
                            else:
                                print ("There is not a man here.")
                        else:
                            kode2469_brukt = True 
                            print ("Denne koden fungerer bare en gang, prøv en annen kode.")


                    else:
                        print("Feil kode! Låsen lager en merkelig lyd. Prøv å finne ut hva koden er ved å undersøke ting i rommet.")

        # Sjekker om spilleren har trykket på en tast
        elif event.type == pygame.KEYDOWN:
            # Sjekker om spilleren har trykket på 'i'-tasten
            if event.key == pygame.K_i:
                # Bytter mellom true og false. Det åpner og lukker inventaret
                inventar_apen = not inventar_apen
            
            # Lukke vindu og inventar med ESC-tasten
            elif event.key == pygame.K_ESCAPE:
                if vindu_apnet:
                    vindu_apnet = False
                    print("Du lukket utsikten.")
                elif inventar_apen:
                    inventar_apen = False
    
    
    # ============================================
    # TEGNER OPP TING I KLASSEROMMET
    # ============================================
    screen.fill((220, 230, 240))
    # --- Gulv ---
    pygame.draw.rect(screen, (160, 120, 80), (0, 600, 1100, 150)) #Gulv
    
    # --- Tavle ---
    pygame.draw.rect(screen, (100, 65, 35), (240, 330, 420, 180)) #Tavleramme
    pygame.draw.rect(screen, (40, 100, 70), (250, 340, 400, 160)) #Tavle
    # Tekst skrevet på tavla med kritt (hvit farge)
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
    
    # --- Pult ---
    pygame.draw.rect(screen, (120, 80, 40), (300, 580, 200, 15))    # Bordplate
    pygame.draw.rect(screen, (80, 80, 80), (320, 595, 12, 50))      # Bein venstre
    pygame.draw.rect(screen, (80, 80, 80), (476, 595, 12, 50))      # Bein høyre

    # --- Stolen til pult 1 ---
    pygame.draw.rect(screen, (100, 100, 100), (360, 610, 70, 12))   # Sete
    pygame.draw.rect(screen, (100, 100, 100), (360, 550, 12, 60))   # Stolrygg
    pygame.draw.rect(screen, (60, 60, 60), (370, 622, 8, 25))       # Stolbein venstre
    pygame.draw.rect(screen, (60, 60, 60), (412, 622, 8, 25))       # Stolbein høyre
    
    # --- Kommode ---
    pygame.draw.rect(screen, (100, 60, 25), (850, 480, 110, 120))   # Kommodens ramme
    
    # Åpent skap med ":3" risset inn 
    if skap_apnet:
        pygame.draw.rect(screen, (50, 30, 10), (860, 535, 90, 55))  # Mørk bakvegg inni skapet
        skap_tekst = skrift.render(":3", True, (200, 180, 140))     # ":3" på bakveggen
        screen.blit(skap_tekst, (890, 550))
    else:
        # Lukket skap
        pygame.draw.rect(screen, (115, 75, 35), (860, 535, 90, 55))    # Skapdør
        pygame.draw.circle(screen, (210, 175, 70), (940, 562), 4)      # Håndtak på skapdøren

    # Åpen skuff
    if skuff_apnet:
        pygame.draw.rect(screen, (90, 55, 20), (840, 490, 90, 38))   # Skuffen dratt ut
        skuff_tall = skrift.render("9", True, (240, 230, 200))       # Tallet 9 risset inn
        screen.blit(skuff_tall, (880, 497))
    else:
        # Lukket skuff
        pygame.draw.rect(screen, (115, 75, 35), (860, 490, 90, 38))  # Skuff 
        pygame.draw.circle(screen, (210, 175, 70), (905, 509), 4)    # Håndtak på skuffen

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

    # --- VISER BILDET "tree.gif" HVIS VINDUET ER ÅPNET ---
    if vindu_apnet:
        # Mørk bakgrunn bak bildet
        pygame.draw.rect(screen, (20, 20, 20), (230, 100, 640, 520))
        pygame.draw.rect(screen, (200, 200, 200), (230, 100, 640, 520), 3)
        
        if tree_bilde:
            # Tegner bildet midt på skjermen
            screen.blit(tree_bilde, (250, 120))
        else:
            # Hvis bildet mangler kommer det feilmelding
            feil_tekst = skrift.render("Fant ikke 'tree.gif' i mappen!", True, (255, 100, 100))
            screen.blit(feil_tekst, (380, 330))
            
        # Tekst under bildet som forklarer hvordan man kan lukke bildet med treet igjen. 
        lukk_info = skrift.render("Klikk på vinduet eller trykk [ESC] for å lukke", True, (255, 255, 255))
        screen.blit(lukk_info, (340, 570))

    pygame.display.flip()

pygame.quit()