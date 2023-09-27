#Toets 

#Opdracht 1:


#a: Waarom is Visual Studio Code handiger voor software development dan bijvoorbeeld Notepad (kladblok)? Noem de voordelen!
# - VS code is gemaakt voor het programmeren maar een kladbok is alleen maar de tekst editen.
# - VS Code is sterk uitbreidbaar door middel van extensies. 
# - Je kunt opdrachten uitvoeren en niet bij notepad.

#b: Waarom is het goed dat je de commits van jouw code pusht naar github.com?
# Hierdoor creër je backup voor je code uit je lokale sd.
 

#Opdracht 2:

# Maak het commentaar af.
a = 5  # dit is een voorbeeld van het datatype: integer (geheel getal)
b = 10.5# dit is een voorbeeld van het datatype: float (komma getal)
c = "Hallo wereld" # dit is een voorbeeld van het datatype: string (tekenreeks!)

#Opdracht 3:

# Schrijf code die de waarden van a en b omwisselt. 
a = 5
b = 10
# Extra variabele:
wissel = a
a = b
b = wissel

print(f"a = {a}, b = {b}") # Moet "a = 10 b = 5" printen > succes!

#Opdracht 4:

# Hier moest int erbij!
leeftijd = int(input("Hoe oud ben je?"))
#Hier heeft 67 - leeftijd geen variabele dus eentje ff maken!
min67 = 67 - leeftijd #En dit zijn ook weer de verkeerde haakjes!
print(f"Dan duurt het nog ongeveer {min67} jaar voordat je met pensioen mag!")
# Is 18 ingevuld? Dan zie je op de terminal: Dan duurt het nog ongeveer 49 jaar voordat je met pensioen mag!

#Opdracht 5: 
# Schrijf een functie die 3 getallen bij elkaar optelt en zorg ervoor
# dat de uitkomst ervan wordt getoond in de print
def som(a,b,c):
    return a + b+ c
getal1 = 200
getal2 = 5
getal3 = 12
antwoord = som(getal1, getal2, getal3)# of de naam van je eigen functie.
print(f"De som van {getal1} + {getal2} + {getal3} = {antwoord}")

#Opdracht 6
# Maak de volgende code af:# Je moet bijbetalen als je over je minuten of je GB's heen gaat en geen onbeperkt abonnement hebt.
AANTAL_GB = 20 # Aantal GB data in je bundel
AANTAL_MINUTEN = 200 # Aantal belminuten in je bundel
ONBEPERKT = True # test ook met True
aantal_minuten_gebeld = int(input("Hoeveel minuten heb je gebeld?"))
aantal_GB_internet = int(input("Hoeveel GB's heb je gebruikt?"))
bijbetalen = (aantal_minuten_gebeld > AANTAL_MINUTEN or aantal_GB_internet > AANTAL_GB) and not ONBEPERKT

if bijbetalen:
    print("Let op: je moet bijbetalen!")
else:
    print("Niks aan de hand gebruik je mobiel lekker verder!")
 
#Opdracht 7
# Print onder elkaar de getallen 1-250 met max 2 regels code.  
for getal251 in range(1, 251):
    print(getal251)

#Opdracht 8
# Gegeven is:

lijst_eten = ['appel', 'pannenkoek', 'kiwi', 'hamburger']
# a: print een eenvoudig menu met de volgende layout:
print("Onze menukaart:")
for item in lijst_eten:
    print(item)
# Onze menukaart:
# appel
# pannenkoek
# kiwi
# hamburger 

# b: Schrijf code die ervoor zorgt dat alleen het eten met de langste naam wordt geprint in de terminal.
langste_eten = max(lijst_eten, key=len)

print(f"Het eten met de langste naam is: {langste_eten}")

#Opdracht 9
while True:
    try:
        invoer = int(input("Voer een getal tussen de 0 en 10 in:"))
        if 0 <= invoer <= 10:
            print(f"Je hebt {invoer} ingevoerd!")
            break
        else:
            print("Error: voer een getal tussen de 0 en 10 in!")
    except ValueError:
        print("Fout: dit is geen geldig getal. Probeer opnieuw!")

#Opdracht 10
#Deze heeft te maken met if elif else en int plus max moet anders.
MAX = 20
getal = int(input("Voer een getal in:"))

if getal > MAX:
    print(f"Het getal is groter dan {MAX}")
elif getal < MAX:
    print(f"Het getal is kleinder dan {MAX}")
else:
    print(f"Het getal is gelijk aan {MAX}")