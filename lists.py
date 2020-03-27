# lists
# Listen sind mutable!

leereListe = []
meineListe = [1,2,3,4,5]

# Wieviele Elemente hat die Liste?
print(len(meineListe))  # 5
print(meineListe)   # [1, 2, 3, 4, 5]
meineListe[1] = meineListe[1] + 10
print(meineListe)   # [1, 12, 3, 4, 5]

# auch unterschiedliche Datentypen sind möglich
meineListe = ['Text', 3.1415 , 12, 'Hallo', 'Welt']
print(meineListe)   # ['Text', 3.1415, 12, 'Hallo', 'Welt']

# Zugriff über Index (nullbasiert)
print(meineListe[2]) # 12

# auch Slicing geht
print(meineListe[1:4])  # [3.1415, 12, 'Hallo']
# Slicing Operationen geben neue Liste zurück (also Kopie)

# Listen in Listen ... (nested lists)
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

print(4 * meineListe) # [1, 2, 3, 11, 12, 13, 1, 2, 3, 11, 12, 13, 1, 2, 3, 11, 12, 13, 1, 2, 3, 11, 12, 13]

# Eintrag aus einer Liste löschen
meineListe = [1,2,3,4,5,6,7]
print(meineListe)   # [1, 2, 3, 4, 5, 6, 7]
meineListe.pop()    
print(meineListe)   # [1, 2, 3, 4, 5, 6]
meineListe.remove(5)   
print(meineListe)   # [1, 2, 3, 4, 6]
del meineListe[3:5]
print(meineListe)   # [1, 2, 3]

# Slicing 
# flache Kopie einer Liste
meineListe = [1,2,3,4,5,6]
neueListe = meineListe[:]
print(id(meineListe), id(neueListe)) # unterschiedliche Id's
meineListe[4:6] = []    # 2 Elemente entfernen
print(meineListe)       # [1, 2, 3, 4]
meineListe[:] = []      # Liste mit Slicing leeren
print(meineListe)       # []

# Anhängen an eine Liste
meineListe = [1,2,3,4]
meineListe.append(5)
meineListe.append(['a','b'])
print(meineListe)   # [1, 2, 3, 4, 5, ['a', 'b']]
meineListe.extend([7,8,9])  # mehrere Elemente anhängen
print(meineListe)   # [1, 2, 3, 4, 5, ['a', 'b'], 7, 8, 9]

# aus range(...) eine Liste machen
an_list=range(10)
print(an_list)          # range(0, 10)
an_list=list(an_list)
print(an_list)          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Liste umkehren

an_list.reverse()
print(an_list)          # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
