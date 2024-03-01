import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import random
import shutil
from concurrent.futures import ThreadPoolExecutor


def load_copy_data(path):

    # fais une copie dun dossier , récupere les liens des elements dans le dossier 
    shutil.copytree(path, path+"_copy",dirs_exist_ok=True)

    path+="_copy"

    # recupere les images du dossier copié
    yes = [ os.path.join(path+"/yes", filename) for filename in os.listdir(path+"/yes")]
    no = [ os.path.join(path+"/no", filename) for filename in os.listdir(path+"/no")]
    
    return yes,no



def image_formatting (path,dim):

    # load image 
    img = cv2.imread(path)
    
    #cropping 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)    
    max_contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(max_contour)
    cropped = img[y:y+h, x:x+w]
    
    # resize
    resize=cv2.resize(cropped, (dim[0],dim[1]), interpolation = cv2.INTER_AREA)
     
    # Appliquer un flou gaussien pour réduire le bruit
    blurred = cv2.GaussianBlur(resize, (5, 5), 0)

    # sauvegarde 
    cv2.imwrite(path, blurred)  


def shape(path): return np.array (cv2.imread(path).shape)


def preprocessing(path):

    #image de scanner separer
    yes,no=load_copy_data(path)
    print(yes)

    # taille de l'ensmeble
    size=len(yes)+len(no)
   
    #dimensions des images 
    dim_data=[shape(x) for x in yes+no]

    # moyenne des dimensions des images 
    mean_data= [round(x) for x in sum(dim_data)/size][0:2]

    with ThreadPoolExecutor(max_workers=os.cpu_count()-1) as executor:
        executor.map(lambda x : image_formatting(x,mean_data),yes+no)



def split_data (data, train_size=0.7,test_size=0.15,val_size=0.15):

    if  train_size+test_size+val_size >1 : 

        raise "la somme des partie doit valoir 1"

    else : 

        random.shuffle(data)

        train_set = data[:int(len(data)*train_size)]
        test_set =  data[:int(len(data)*test_size)]
        val_set = data[:int(len(data)*val_size)]

    return train_set,test_set,val_set
                










     


