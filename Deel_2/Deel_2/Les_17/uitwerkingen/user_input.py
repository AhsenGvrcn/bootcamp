#Zoals de practice bestand met def, while true, try, expect, prompt + value.
def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
          print("Ongeldige invoer. Voer een geheel getal in.")

def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
          print("Ongeldige invoer. Voer een getal in.")

def get_string(prompt):
    value = input(prompt)
    return value

def get_letter(prompt):
    while True:
        value = input(prompt)
        if len(value) == 1 and value.isalpha():
            return value.upper()
        else:
            print("Ongeldige invoer. Voer precies één letter in.")

#Geeft aan wat je hebt ingevoert.

