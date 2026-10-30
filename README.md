#  Escape Room - Klasserommet

Et Escape Room spill laget i Python med Pygame.

##  Om spillet

Du er låst inne i et klasserom og må komme deg ut. Du må undersøke gjenstander i rommet og finne den 4-sifrede koden for å låse opp døra og komme deg ut.

##  Hva du trenger for å spille

1. **Python** installert på datamaskinen.
2. **VS Code** (eller et annet tekstredigeringsprogram).
3. **Pygame**-biblioteket.

##  Nødvendige filer i samme mappe

For at spillet skal fungere optimalt med lyd og bilde, må disse tre filene ligge i **samme mappe**:

* `main.py` – Selve koden til spillet.
* `tree.gif` – Bilde som vises når du ser ut av vinduet.
* `Well, there is a man here..mp3` – Lydfil for vinduet.

*(Dersom bilde- eller lydfilen mangler, vil spillets `try-except`-feilhåndtering sørge for at spillet likevel kjører trygt uten å kræsje).*

##  Slik åpner og kjører du spillet i VS Code

### 1. Åpne mappen i VS Code
* Start VS Code.
* Gå til `File` -> `Open Folder...`  og velg mappen der `main.py`, `tree.gif` og  `Well, there is a man here..mp3` ligger.

### 2. Installer Pygame (om du ikke har det fra før)
* Åpne terminalen inne i VS Code (`Terminal` -> `New Terminal`).
* Skriv inn følgende kommando og trykk Enter:
  `pip install pygame`

### 3. Kjør spillet
* Åpne filen `main.py` i VS Code.
* Klikk på **Play-knappen** øverst til høyre i VS Code, **eller** skriv `python main.py` i terminalen nederst.

## Kontroller i spillet

* **Venstreklikk med musen:** Klikk på ting i rommet (tavle, dør, kommode, bøker, søppelbøtte osv.) for å undersøke dem.
* **Trykk 'i':** Åpner og lukker inventaret ditt.
* **Klikk i inventaret:** Klikk på lappen om du har plukket opp for å lese den.
* **Trykk 'ESC':** Lukker åpne bildevisninger eller inventaret.
* **Terminalen i VS Code:** Når du klikker på døren eller hemmelige koder, må du skrive inn svaret/koden i terminalen nederst i VS Code.