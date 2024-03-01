import numpy as np
import cv2


def shape(path):

    """

        récupere les dimensions d'une images en pixel 

        Args : chemin de l'image
        Return : shape de l'image
    
    """

    image = cv2.imread(path)
    return np.array(image.shape)

