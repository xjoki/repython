# Zufallszahl

import time
def get_rndNmb(n):
    t = time.time()
    rndNumber = int(n * round(t - int(t), 3))
    return rndNumber

print(get_rndNmb(500))
