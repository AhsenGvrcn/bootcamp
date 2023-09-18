import random

aantal_gespeelde_rondes = 0
aantal_fouten = 0

while True:
    aantal_gespeelde_rondes += 1
    willekeurig_getal = random.randint(1, 5)
    fout_geraden = False

    print(f'Ronde {aantal_gespeelde_rondes}')

    while True:
        gebruikers_getal = int(input("Raad het getal tussen 1 en 5: "))

        if gebruikers_getal == willekeurig_getal:
            print("\033[92mJe hebt het getal goed geraden!\033[0m")
            break
        else:
            print("\033[91mJe hebt het getal niet goed geraden. Probeer opnieuw!\033[0m")
            aantal_fouten += 1
            fout_geraden = True

    antwoord = input("Wil je nog een ronde spelen? (ja/nee: )")
    if antwoord.lower() != "ja":
        break
print(f"Je hebt {aantal_gespeelde_rondes} rondes gespeeld.")
print(f"Je hebt {aantal_fouten} keer fout geraden.")