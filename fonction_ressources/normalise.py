import cv2
import numpy as np

def normalise_images(X, target_size):
    # Liste pour stocker les images normalisées
    normalized_images = []

    # Parcourir les images
    for image in X:
        # Redimensionner l'image en conservant le rapport d'aspect
        height, width = image.shape[:2]
        if height > width:
            new_height = target_size[1]
            new_width = int(width * (target_size[1] / height))
        else:
            new_width = target_size[0]
            new_height = int(height * (target_size[0] / width))
        
        image_resized = cv2.resize(image, (new_width, new_height))

        # Convertir en niveaux de gris
        gray = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)

        # Calculer l'histogramme de l'image en niveaux de gris
        hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

        # Calculer la luminosité moyenne et l'écart type du contraste
        mean_brightness = np.mean(gray)
        mean_contrast = np.std(gray)

        # Appliquer une accentuation adaptative des bords
        sharpened_image = cv2.detailEnhance(image_resized, sigma_s=10, sigma_r=0.15)

        # Identifier le contour du cerveau
        _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Dessiner un rectangle jaune autour du cerveau et recadrer l'image
        if contours:
            x, y, w, h = cv2.boundingRect(contours[0])
            if w > 10 and h > 10:  # Vérifier si le contour est suffisamment grand
                cv2.rectangle(sharpened_image, (x, y), (x+w, y+h), (0, 255, 255), 2)
                adjusted_image_cropped = sharpened_image[y:y+h, x:x+w]
                # Redimensionner à nouveau l'image proportionnellement
                adjusted_image_cropped_resized = cv2.resize(adjusted_image_cropped, target_size)
                normalized_images.append(adjusted_image_cropped_resized)
            else:
                # Si le contour est trop petit, ajouter l'image originale
                normalized_images.append(image_resized)
        else:
            # Si aucun contour n'est trouvé, ajouter l'image originale
            normalized_images.append(image_resized)

    return normalized_images