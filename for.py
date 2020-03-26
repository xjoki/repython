# for

myList = ['Hund', 'Katze', 'Maus']
for entry in myList:
    print(entry, end=' ')

print()

# Nutzung der Funktion range
# 0 1 2 3 4 5 6 7 8 9
for i in range(10):
    print(i, end=' ')   

# 0 1 2 3 4 5 6 7 8 9 0 2 4 6 8 10 12 14 16 18
for i in range(0, 20, 2):   # start, stop, step
    print(i, end=' ')   

print()

# Nutzen der Funktion enumerate()
# 0 Hund
# 1 Katze
# 2 Maus
for i, theValue in enumerate(myList):
    print(i, theValue)


for n in range(30, 40):
     for x in range(2, n):
         if n % x == 0:
             print(n, '=', x, '*', n//x)
             break
     else:  # ! else: gehört zur for-Schleife !!! nicht zum if !
         # Schleife wurde durchlaufen, ohne dass ein Faktor gefunden wurde
         print(n, 'ist eine Primzahl')

