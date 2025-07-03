import os
import pickle

filename= "account.dat"

def check_file(filename):
    return os.path.exists(filename)


def read_from_file(filename):
    if check_file(filename):
        if os.path.getsize(filename)>0:
            file=open(filename, "rb")
            try:
                data_list=[]
            except EOFError:
                data_list=[]
            finally:
                file.close()
            return data_list
        else:
            return []

    else:
        file = open(filename, "wb")
        file.close()
        return []

def write_to_file(filename, data_list):
    file = open(filename, "wb")
    pickle.dump(data_list, file)
    file.close()
