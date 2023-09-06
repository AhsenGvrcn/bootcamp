#Deed een recap van een les dat hierover was, variabele maken van studenten, collegegeld, de totale bedrag, appels, druiven en bananen. + de btw!
studenten= 21
collegegeld= 1150
totaal= collegegeld*studenten
print(totaal)  #Geeft de resultaat 24150.
appels= 3.40
druiven= 2.45
bananen= 1.95
#Hier de totale fruit kosten..
totaal_fruit= appels+druiven+bananen
btw_9= 0.09 #De btw op fruit in Nederland is 9%, 100%=1 > 9%= 0.09
btw_bedrag= totaal_fruit*btw_9 #De btw bedrag van het fruit!
totaal_bedrag_btw= totaal_fruit + btw_bedrag
#nu dat we alle informatie hebben printen we de totale bedrag inclusief BTW voor her fruit!
print("Totaalbedrag inclusief BTW op fruit van 9%:", totaal_bedrag_btw )