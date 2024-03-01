from shape import shape 
import matplotlib.pyplot as plt 


def statistique (data):

    """
        calculs differentes informations sur une liste d'image,
        comme le taille de l'esemble, la medianne et la moyenne des dimensions

        Args: liste [np.array]
        return : None
    
    """

    # taille de l'ensembles
    size=len(data)

    #dimensions des images 
    dim_data=[shape(x)[:2] for x in data]

    # sort des dimensions
    sort_dim_data=sorted(dim_data, key= lambda x : (x[0],x[1]))

    # moyenne des dimensions des images 
    mean_data= [round(x) for x in sum(dim_data)/size][0:2]

    #  mediane des dimensions des images 
    mediane_data=[round(x) for x in sort_dim_data[size//2]][0:2]

    print("moyenne des resolutions",mean_data)
    print("mediannes des resolutions",mediane_data)

    # graphiques de repartitions des resolutions d'image 
    plt.plot(sort_dim_data)



   
    