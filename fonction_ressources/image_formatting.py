import cv2

def image_formatting (path,dim):

    # load image 
    img = cv2.imread(path)
    
    #cropping 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    # _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  
    # contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)    
    # max_contour = max(contours, key=cv2.contourArea)
    # x, y, w, h = cv2.boundingRect(max_contour)
    # cropped = img[y:y+h, x:x+w]
    
    # resize
    resize=cv2.resize(gray, (dim[0],dim[1]), interpolation = cv2.INTER_AREA)
     


    # sauvegarde 
    cv2.imwrite(path, resize)  
