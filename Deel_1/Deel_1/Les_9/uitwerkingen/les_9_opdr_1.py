a = 5
b = 3
c = 2
if (a==6 and b==4 or c==2):
   print("De conditie is waar")
else: 
   print("De conditie is niet waar")

#Het verschil zit in de haakjes bij b en c. In de tweede code zitten de haakjes anders. In het eerste codefragment worden de operatoren is eerst "and" en vervolgens "or" gebruikt.
#In het tweede codefragment worden haakjes gebruikt om de prioriteit te bepalen. In het tweede codefragment worden haakjes gebruikt om de prioriteit te bepalen.
#Sinds in Wiskunde je altijd eerst de haakjes verwerkt zal de programma hetzelfde doen en dat prioriëren. Hierdoor komen er verschillende uitkomsten.
a = 5
b = 3
c = 2
if (a==6 and (b==4 or c==2)):
   print("De conditie is waar")
else:
   print("De conditie is niet waar") 