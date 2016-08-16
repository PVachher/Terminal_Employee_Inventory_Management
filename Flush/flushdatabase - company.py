import pickle
def flushfile():
    k = {}
    k['sales'] = {}
    k['company'] = 0
    pickle.dump(k, open("../Databases/companymanagement.db","wb"))
flushfile()