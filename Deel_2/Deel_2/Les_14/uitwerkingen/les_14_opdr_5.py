namenlijst = ['Ahsen', 'Natalia', 'Aliyah', 'Shankaroon', 'Efsun']
naam = input("Voer een naam in: ")

if naam in namenlijst:
    namenlijst.remove(naam)
else:
    namenlijst.append(naam)
    print(f'{naam} is toegevoegd aan de lijst.')

print("De bijgewerkte lijst met namen is: ")
print(namenlijst)