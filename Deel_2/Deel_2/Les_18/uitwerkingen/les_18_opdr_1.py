import random

def controleer_bereik(getal, minimum, maximum):
    return minimum <= getal <= maximum

aantal_gespeelde_rondes = 0
aantal_fouten = 0
min_bereik = 1
max_bereik = 5

while True:
    aantal_gespeelde_rondes += 1
    willekeurig_getal = random.randint(min_bereik, max_bereik)
    fout_geraden = False

    print(f"Ronde {aantal_gespeelde_rondes}")

    while True:
        gebruikers_getal = int(input(f"Raad het getal tussen {min_bereik} en {max_bereik}: "))
        
        if not controleer_bereik(gebruikers_getal, min_bereik, max_bereik):
            print(f"Voer een getal in tussen {min_bereik} en {max_bereik}")
            continue #Vraagt opnieuw!
       
        if  gebruikers_getal == willekeurig_getal:
            print("\033[92mJe hebt het getal goed geraden!\033[0m")
            break
        else:
           print("\033[91mJe hebt het getal niet goed geraden. Probeer opnieuw!\033[0m")  # Rode tekst (code 91m)
           aantal_fouten += 1
           fout_geraden = True

    antwoord = input("Wil je nog een ronde spelen? (ja/nee): ").lower()
    if antwoord != "ja":
        break

    
