import random

willekeurig_getal = random.randint(1, 5)

gebruikers_getal = int(input("Raad het getal tussen 1 en 5: "))

if gebruikers_getal == willekeurig_getal:
    print("\033[92mJe hebt het getal goed geraden!\033[0m")  #Groene tekst code 92m
else:
    print("\033[91mJe hebt het getal niet goed geraden!\033[0m") #Rode tekst code 91m