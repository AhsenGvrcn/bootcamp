import random

for ronde in range(1 , 4):
   print(f"Ronde {ronde}")
   willekeurig_getal = random.randint(1, 5)

   while True:
    gebruikers_getal = int(input("Raad het getal tussen 1 en 5: "))

    if gebruikers_getal == willekeurig_getal:
      print("\033[92mJe hebt het getal goed geraden!\033[0m")  #Groene tekst code 92m
      break

    else:
      print("\033[91mJe hebt het getal niet goed geraden!Probeer opnieuw!\033[0m") #Rode tekst code 91m