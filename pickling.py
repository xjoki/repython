# Pickling / Unpickling
# Persistenz

import pickle

hash = { 'toll':1, 'gut':2, 'ok':3, 'geht noch':4, 'schlecht':5, 'extrem schlecht':6 }
with open('workfile','wb') as f:
    pickle.dump(hash, f)
f.close()

with open('workfile','rb') as f:
    print(pickle.load(f))
f.close()