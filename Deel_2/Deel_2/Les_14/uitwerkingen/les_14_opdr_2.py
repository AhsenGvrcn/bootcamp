getallenlijst = [10,20,30,40,50]
index = int(input("Voer een index in om een getal te verwijderen: "))

if index >= 0 and index < len(getallenlijst):
    verwijderd_getal = getallenlijst.pop(index)
    print(f'Het verwijderde getal is: {verwijderd_getal}')
    print("De bijgewerkte lijst is: ")
    print(getallenlijst)
else:
    print("Ongeldige index. Voer een index tussen de 0 tot 4.")