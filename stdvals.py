# Standardwerte
# stdvals

def myFunc1(name="Doe", firstname="John"):
    print(name, firstname)

myFunc1()                   # Doe John
myFunc1("Joki")             # Joki John
myFunc1("Oki", "Doki")      # Oki Doki
# Verwendung Schlüsselwort-Argument
myFunc1(firstname="Doki")   # Doe Doki

