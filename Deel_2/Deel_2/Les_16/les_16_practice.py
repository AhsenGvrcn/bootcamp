def divide (getal1,getal2, operator):
  if operator == "/":
    result = getal1/getal2
  elif operator == "*":
    result = getal1 * getal2
  else:
    result = 0

  return result   #dit kan ook zoals product maar dan alleen divide!


def product (getal1, getal2):
  result = getal1 * getal2 
  return result                          #we willen dat hij de result geeft anders geeft die een nul.

g1 = int(input('getal1?'))
g2 = int(input('getal2?'))

print(product(g1,g2))
print( product(16,5))
print( product(24,2))
print( product(1,50))
print( product(34,58))
         #dit is de input van een function!





#lenght = len(('aap noot mies') * 12)

#print(lenght)