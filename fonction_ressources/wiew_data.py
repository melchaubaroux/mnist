import cv2
import matplotlib.pyplot as plt 


def wiew_data(data,name):

    plt.figure(figsize=(50, 50),dpi=80)

    for i in range(1, min(len(data),20)):
        image = cv2.imread(data[i])
        plt.subplot(5, 4, i)
        plt.imshow( image, cmap='gray')
        plt.title(data[i][data[i].index("copy")+5:data[i].index("copy")+8])

    plt.suptitle(name, fontsize=80)
       
    plt.show()
