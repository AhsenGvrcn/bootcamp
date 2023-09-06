#Hoeveel seconden zitten er in een dag? Pak alle informatie.
seconden= 60 #per minuut
minuten= 60 #per uur
uren= 24 #per dag
totaal= seconden*minuten*uren
#De resultaat: (geeft 86400 seconden.)
print("Er zitten", totaal, "seconden in een dag.")

#In een week is dat..
week= 7 #In een week zitten er 7 dagen.
aantal_uren= week*uren
totaal_week= seconden*minuten*aantal_uren
#De resultaat: (geeft 604800 seconden.)
print("Er zitten", totaal_week, "seconden in een week.")

#In een jaar is dat..
dagen_jaar= 365
uren_jaar= dagen_jaar*uren
totaal_jaar= seconden*minuten*uren_jaar
#De resultaat: (geeft 315360000 seconden.)
print("Er zitten", totaal_jaar,"seconden in een jaar." )