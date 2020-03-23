# Mengen

menge1 = {1,2,3,4,5}    
menge2 = {5,4,3,2,1}

print(menge1 == menge2)     # True

# Zugriff auf Elemente über Index NICHT möglich!!! (object is not subscriptable)
# print(menge1[2])   funktioniert nicht!

# Hinzufügen von Elementen
menge1.add(6)   # immer nur eines!
print(menge1)   # {1, 2, 3, 4, 5, 6}
menge1.remove(6)    
print(menge1)   # {1, 2, 3, 4, 5}

menge1 = {2,4,6,8,10,12,14,16,18,20}
menge2 = {3,6,9,12,15,18}
menge3 = {6,8,12}
print(menge3.issubset(menge1)) # True
print(menge2.difference(menge1)) # {9, 3, 15}

zus_menge = menge1.union(menge2)
print(zus_menge)    # {2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20}

