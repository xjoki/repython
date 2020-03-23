# Primzahlen

import math
def isPrime(value):
    if value < 0:
        return False
    for i in range(2, int(math.sqrt(value)) + 1):
        if value % i == 0:
            return False
    return True

m = set()

for i in range(1, 100):
    if isPrime(i) == True:
        m.add(i)

print(m)    