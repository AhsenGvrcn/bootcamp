oppervlakte = int(input('Hoeveel m2 vloerbedekking heeft u nodig?'))
prijs_m2 = 40

if oppervlakte >= 150: #double if zou een probleem aangeven, bij het gebruiken van elif, zou je met specifiek kunnen zijn.
    prijs_m2 = 35
elif oppervlakte >= 80:
    prijs_m2 = 38

totaal = prijs_m2 * oppervlakte

print(f'Het totaalbedrag is voor een oppervlakte van {oppervlakte} m2 is: Eur ' + str(totaal))