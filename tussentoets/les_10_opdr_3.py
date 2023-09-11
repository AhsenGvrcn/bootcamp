naam = input("Wat is je naam?")
zin = f"Hoi {naam}, wat is je leeftijd?"
leeftijd = int(input(zin))

if leeftijd < 18:
    print(f"Beste {naam}, je bent nog geen 18. Alleen autorijden zit er dus niet in :-(" )
else: #Ouder dan 18 of verder..
    print(f"Beste {naam}, je bent 18 of ouder en mag dus alleen autorijden (met rijbewijs althans).")
 
