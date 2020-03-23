# lists
leereListe = []
meineListe = [1,2,3,4,5]
print(meineListe)

# auch unterschiedliche Datentypen sind möglich
meineListe = ['Text', 3.1415 , 12, 'Hallo', 'Welt']
print(meineListe)

# Zugriff über Index (nullbasiert)
print(meineListe[2]) # 12

# auch Slicing geht
print(meineListe[1:4])  # [3.1415, 12, 'Hallo']

# Listen in Listen ...
nList = [1, [1,2,[9,8],3], 2, [4,5,6]]
print(nList)

x = 0
meineListe = range(10)

for i in meineListe:
    x += meineListe[i]

print(x)    # 45
print(22 in meineListe) # False

meineListe = [12,11,13] + [3,2,1]
print(meineListe)   # [12, 11, 13, 3, 2, 1]

# Liste sortieren
meineListe.sort()
print(meineListe)   # [1, 2, 3, 11, 12, 13]