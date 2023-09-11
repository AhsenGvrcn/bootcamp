
from time import sleep # je hoeft nog niet te weten wat een import is, Kopieer deze regel en je kunt je programma laten wachten met de opdracht sleep(x seconden)


oppervlakte = int(input('Hoeveel m2 vloerbedekking heeft u nodig?'))
prijs_m2 = 40
AANT_MELDINGEN = 5 #Informatie in de opdracht zelf, dit is hoe vaak je de melding wil :D!! Dit kan je anders constant maken.

print("Een moment geduld a.u.b., de scherpste prijs wordt berekend.")

meldingen = 0 #De teller!! 

while meldingen < AANT_MELDINGEN:
    sleep(1)
    print("Een moment geduld a.u.b., de scherpste prijs wordt berekend.")
    meldingen += 1

totaal = prijs_m2 * oppervlakte


# secret code containing the answer of question 4

# end of secret



print(f'Het scherpste prijs voor een oppervlakte van {oppervlakte} m2 is: Eur ' + str(totaal))