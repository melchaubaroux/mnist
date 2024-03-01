import numpy as np
import os
from concurrent.futures import ThreadPoolExecutor
from  image_formatting import image_formatting




def preprocessing(data,dim):

    """
        prend une liste de d'image et applique la fonction de formatage d'une image 

        Args : liste image 

        return None 
 
    """

    with ThreadPoolExecutor(max_workers=os.cpu_count()-1) as executor:
        executor.map(lambda x : image_formatting(x,dim),data)









     


