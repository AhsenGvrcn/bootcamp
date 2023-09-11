#Zoals in practice, do je int en input.
cijfer = int(input("Voer je cijfer in: "))
#Dit is dan de omschrijving variabele! Je gebruikt if, elif, else :D
 
if cijfer == 10:
    omschrijving = "Uitmuntend"
elif cijfer == 9:
    omschrijving = "Zeer goed"
elif cijfer == 8:
    omschrijving = "Goed"
elif cijfer == 7:
    omschrijving = "Ruim voldoende"
elif cijfer == 6:
    omschrijving = "Voldoende"
elif cijfer == 5:
    omschrijving = "Bijna voldoende"
elif cijfer == 4:
    omschrijving = "Onvoldoende"
elif cijfer == 3:
    omschrijving = "Gering"
elif cijfer == 2:
    omschrijving = "Slecht"
elif cijfer == 1:
    omschrijving = "Zeer slecht"
else:
    omschrijving= "Ongeldig cijfer"
#Aantekening = je wilt hem houden dus doe je geen print maar de omschrijving aka variabele, printen houdt het niet is dan totaal, end.
#Verder met opdracht 2, hoort erbij.
#Gebruik je aantekeningen> weer if, elif, else!

if cijfer >= 6:
    print(f"Gefeliciteerd, {omschrijving} je resultaat is een {cijfer}")
elif cijfer <= 6:
    print(f"Jammer, {omschrijving} je resultaat is een {cijfer}")
else: 
    print("Dit kan ik niet")
