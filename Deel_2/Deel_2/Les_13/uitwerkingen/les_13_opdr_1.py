#Tuple is een lijstje van verschillende dingen. Staat in practice.py.
kleuren_tuple = ('rood','zwart', 'blauw', 'groen', 'geel', 'paars', 'oranje')
#De code die nodig is om te vragen voor de naam en welke kleur de gebruiker wilt!
naam = input('Hoe heet je?')
favoriete_kleur = input('Wat is jouw favoriete kleur?')
#Hoeft geen int vanwege het een woord is en geen cijfer.
#Nu doe je wat je bij andere lessen hebt gedaan!
if favoriete_kleur.lower() in kleuren_tuple:
    print(f"{naam}, {favoriete_kleur} is ook een geweldige kleur!")
else:
    print(f"{naam}, helaas {favoriete_kleur} staat niet in de lijst met kleuren. Deze kleur is niet zo geweldig!")
