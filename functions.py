# Functions

def myFunction():
    print("Meine Funktion!")

def funcWithArgs(a, b, c):
    print(a, b, c)

def retVal(a, b):
    return a + b

def retVals(a, b, c, d):
    v1 = a + b
    v2 = c + d
    v3 = a + d
    v4 = b + c
    return v1, v2, v3, v4

# Funktionen aufrufen
myFunction()
funcWithArgs(1, 2, 3)
x = retVal(1, 2)         # 3
print(x)     
print(retVals(1, 2, 3, 4)) # (3, 7, 5, 5)

# Speicherstelle einer Funktion
print(myFunction)   # <function myFunction at 0x...>
