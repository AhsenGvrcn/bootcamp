fruitlijst = ['appel','banaan','druiven', 'kers','kiwi']
verwijderen_fruit = input("Voer een fruitsoort om te verwijderen: ")

if verwijderen_fruit in fruitlijst:
    fruitlijst.remove(verwijderen_fruit)

    print(f'{verwijderen_fruit} is verwijderd uit de lijst: ')
    print("De bijgewerkte lijst met fruiten is: ")
    print(fruitlijst)
else:
    print(f"{verwijderen_fruit} komt niet voor in de lijst van fruitsoorten. ")