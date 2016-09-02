import pickle
def flushfile():
    k = {}
    pickle.dump(k, open("../Databases/employeedatabase.db","wb"))
flushfile()