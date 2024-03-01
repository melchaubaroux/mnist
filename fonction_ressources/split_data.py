import random

def split_data (data, train_size=0.7,test_size=0.15,val_size=0.15):

    if  train_size+test_size+val_size >1 : 

        raise "la somme des partie doit valoir 1"

    else : 

        random.shuffle(data)

        train_set = data[:int(len(data)*train_size)]
        test_set =  data[:int(len(data)*test_size)]
        val_set = data[:int(len(data)*val_size)]

    return train_set,test_set,val_set
                





