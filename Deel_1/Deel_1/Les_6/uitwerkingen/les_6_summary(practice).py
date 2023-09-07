naam = input('Wat is je naam?')

#Hoi Aydin, wat is je leeftijd?
zin = f"Hoi {naam}, wat is je leeftijd?"
leeftijd = int(input(zin))

STUDENTEN_TARIEF = 25 #constanten
STANDAARD_TARIEF = 27.50
SENIOREN_TARIEF = 35
prijs = STANDAARD_TARIEF
TEKST = f"Ons abonnement is {prijs}!!! En je krijgt van ons: "
aanbiedings_zin = ''





#dus o.b.v. leeftijd moet er een aanbieding komen en oh ja, nog geen 18 dan: roep je ouders
#tot 50 is 2GB extra
#vanaf 50 gratis sms
#tot 25 jaar studenten
# vanaf 50 senioren_tarief
if leeftijd < 18:
   aanbiedings_zin="Je mag helaas zelf nog geen abonnement afsluiten!"
elif leeftijd < 50:
    aanbiedings_zin="Je krijgt van ons gratis 2 GB extra data (vanaf 25 BG)"
else: #leeftijd > 50: 
   aanbiedings_zin= "Je krijgt van ons gratis smsjes (zolang de voorraad streekt)"

print(TEKST + " " + aanbiedings_zin)
 # < kleiner dan
 # > groter dan
 #== gelijk aan
 # != niet gelijk aan
 # >= gelijk of groter
 # <= gelijk of kleiner