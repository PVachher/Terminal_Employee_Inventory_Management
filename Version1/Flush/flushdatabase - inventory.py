import pickle
def flushfile():
    k = {}
    pickle.dump(k, open("../Databases/inventorydatabase.db","wb"))
flushfile()