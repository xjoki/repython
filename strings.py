# Stringdefinition in Anführungszeichen oder Hochkomma
# Strings sind immutable!

str1 = 'Hochkomma'
str2 = "Anführungszeichen"

print(str1 + " " + str2)    # Hochkomma Anführungszeichen
print(20 * '-') # --------------------


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

