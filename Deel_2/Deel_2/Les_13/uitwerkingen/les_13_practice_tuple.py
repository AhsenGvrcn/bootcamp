autos = ('fiat','bmw', 'mercedes', 'volkswagen', 'jaguar') #tuple, letterlijk een lijstje! Het zal elke element printen, handige manier om door de elementen de onderdelen van de lijst te lopen.

auto = input('Wat wilt u kopen?')

if auto in autos:
    print('Wat biedt u?')
    #for aanbieding in autos:
       # print(aanbieding) < small practice!
else:
    print('Helaas, daar valt niets aan te verdienen!')

print(autos[2])