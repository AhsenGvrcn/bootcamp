a = float(input("Wat is de waarde van getal a?"))
b = float(input("Wat is de waarde van getal b?"))
#Je neemt de 'if'-'elif'- 'else'.
if a > b:
    print("Variabele a is het grootst want {waarde a} is groter dan {waarde b}")
elif b > a:
    print("Variabele b is het grootst want {waarde b} is groter dan {waarde a}")
else: #a = b
    print("Variabele a en b zijn gelijk.")
  