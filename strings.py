# Stringdefinition in Anführungszeichen oder Hochkomma
# Strings sind immutable!

str1 = 'Hochkomma'
str2 = "Anführungszeichen"

print(str1 + " " + str2)    # Hochkomma Anführungszeichen
print(20 * '-') # --------------------

# raw strings
strRaw = r'Das ist ein/nRaw-String./n'
print(strRaw)   # 'Das ist ein/nRaw-String./n'


print(type(str1))   # <class 'str'>

# ein Zeichen aus dem String
print(str1[2]) # c (!nullbasiert)
# letztes Zeichen
print(str1[-1]) # a
# die letzten 3 Zeichen
print(str1[-3:]) # mma

# Index Error! Index out of range
# print(str1[-222])
# print(str1[len(str1)])    # richtig wäre str1[len(str1)-1]

# das würde nicht gehen: str1[0]='D'
# denn strings = immutable , d.h.
# es wird immer ein neuer String erzeugt!

str3 = str1[-1] + str1[-3:] # amma
print(str3)

# Textlänge
print(len(str2))    # 17

# Slicing
str4 = '0123456789'
print(str4[3:6])    # '345'
print(str4[:5])     # '01234'
print(str4[5:])     # '56789'
print(str4[-5:-1])  # '5678'
print(str4[-5:9])   # '5678'
print(str4[-5:])    # '56789'

text = "Ene mene muh und raus bist du"
suchtext = 'und'
fundstelle = text.find(suchtext)
print(text[fundstelle:fundstelle+len(suchtext)]) # und

# Formatierung
print("Text {} und {}".format("Argument1", "Argument2"))
print("Text {1} und {0}".format("Argument1", "Argument2"))

print("Preis: {:.2f} €".format(14.95733))   # 14.96 €

format1 = '{:10}|{:>10}'    # '>' entspricht rechtsbündig
format2 = '{:10}|{:10.2f} €'
print(format1.format("Produkt", "Preis"))
print(format2.format("Monitor", 379.8762))
print(format2.format("Drucker", 12488.235))

# Produkt   |     Preis
# Monitor   |    379.88 €
# Drucker   |  12488.24 €

# Darstellung in unterschiedlichen Zahlenformaten
myVal = 65535
print('{:b}'.format(myVal))   # binär 1111111111111111
print('{:o}'.format(myVal))   # oktal 177777
print('{:x}'.format(myVal))   # hexadezimal ffff
print('{:X}'.format(myVal))   # hexadezimal (groß) FFFF

# String aufteilen
print(text.split())     # ['Ene', 'mene', 'muh', 'und', 'raus', 'bist', 'du']

# Konvertierung in Groß-/Kleinbuchstaben
print(text.upper(), ',', text.lower())
print("AbCdEfGh".swapcase())    # 'aBcDeFgH'

# Prüfung mit isupper(), islower(), isalpha(), isspace(), isdigit()
# startswith(), endswith()

print('  Text  '.strip())   # 'Text'

