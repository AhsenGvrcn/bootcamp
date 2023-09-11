leeftijd = int(input("Hoe oud ben je?"))
snor = 'j'  # 'j' staat voor ja en 'n' staat voor nee
diploma = 'n'

if (leeftijd >= 18 and snor == 'j') or (leeftijd < 18 and diploma == 'j'):
    print("Je bent aangenomen!")
else:
    print("Je bent niet aangenomen.")
