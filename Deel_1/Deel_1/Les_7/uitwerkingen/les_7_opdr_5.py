euros = 10000 #10.000 euro
rente = 2.8 / 100 #Dit is dan 2.8% rente omgezet in decimaal
#Dit zijn dan de jaren!
jaar_5 = 5
jaar_15 = 15
#Totaal
totaal_5 = euros * (1 + rente) ** jaar_5
totaal_15 = euros * (1 + rente) ** jaar_15
#En dan printen!!
print(f"Na {jaar_5} jaar heb je {totaal_5: .2f} euro.")
print(f"Na {jaar_15} jaar heb je {totaal_15: .2f} euro.")