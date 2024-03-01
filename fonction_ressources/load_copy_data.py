import os 
from make_copy import make_copy_dir

def load_copy_data(path):

    """
        fais une copie d'un dossier et récupere les liens des elements dans le dossier 

        
        Args : chemin du dossier

        Return : liens des elements du sosser
    
    """

    path = make_copy_dir (path)
    print(path)
    yes = [ os.path.join(path+"/yes", filename) for filename in os.listdir(path+"/yes")]
    no = [ os.path.join(path+"/no", filename) for filename in os.listdir(path+"/no")]


    return yes,no