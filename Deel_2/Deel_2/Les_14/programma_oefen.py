# studenten inschrijven
#leeftijd_tuple = (12,15,17,21,13) #tuple & list -> verschillend. Tuple kan je niks afhalen of toevoegen en bij list wel. Dit is een tuple (herken je aan de haakjes.)
leeftijd_lijst = [12,15,17,21,13] #dit is een voorbeeld van een list! Herkenbaar aan de vierkant-achtig haakjes. Deze kun je met de code wijzigen.

leeftijd = 0
while leeftijd == 0:
    try: #wat we proberen
       leeftijd = int(input('Wat is je leeftijd?'))
    except ValueError: #wat dan verkeerd is zoals ->
       print("Voer cijfer in!")
    
 #print("Dit is niet juit uitgevoerd!")           #string-input-string-int > geeft een error aan als he 15 als vijftien in typ, ValueError is der zodat de gebruiker de getal als getal invoert inplaats van in letters.
leeftijd_lijst.append(leeftijd)

print(leeftijd_lijst)

for getal in leeftijd_lijst:
   print(getal)



#andere voorbeeld!'
for aapje in range(5): #lijkt beetje op (0,1,2,3,4)
   print(aapje)                 #gaat dan 1 2 3... onder elkaar printen.