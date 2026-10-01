import numpy as np
import cv2
#Vision Artificial Act 10 NC 0124
# Lee la imagen en escala de grises
img = cv2.imread("nagi.jpg", cv2.IMREAD_GRAYSCALE)
# Abre la ventana con la imagen
cv2.imshow("nagi", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Linea 
print(" LA LINEA 0124")
# Crea una imagen negra
img = np.zeros((512,512,3), np.uint8)

# Dibuja una diagonal blanca de 3px desde una esquina a la otra
img = cv2.line(img,(0,0),(511,511),(255,255,255),3)
# Abre la ventana con la imagen
cv2.imshow("nagi", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Circulo 
print("El circulo 0124")
# Dibuja un circulo azul de radio 10px al centro de la imagen
img = cv2.circle(img, (260,260), 10, (255,0,0),-1)

cv2.imshow("nagi", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Texto
print("El texto 0124")
# Añade a la imagen el texto "Example Text" en color blanco
img = cv2.putText(img, "Alan Romero 0124", (200, 30),cv2.FONT_HERSHEY_SIMPLEX, \
                  0.5, (255, 255, 255), 2)
cv2.imshow("nagi", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Trackbars
print("trackbars")
def on_trackbar(val):
  print(val)

# Crea a una imagen negra, y una ventana llamada 'frame'
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('frame')

# Crea tres trackbar en frame, llamados R,G,B, que van de 0 a 255 y llaman a on_trackbar()
cv2.createTrackbar('R','frame',0,255,on_trackbar)
cv2.createTrackbar('G','frame',0,255,on_trackbar)
cv2.createTrackbar('B','frame',0,255,on_trackbar)

while(True):
    cv2.imshow('frame',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # Obtiene las posiciones de los trackbars
    r = cv2.getTrackbarPos('R','frame')
    g = cv2.getTrackbarPos('G','frame')
    b = cv2.getTrackbarPos('B','frame')

    img[:] = [b,g,r]

cv2.destroyAllWindows() 
cv2.imshow("nagi", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Thresholding
print("Theresholding")
img = cv2.imread('image1.png',0)

ret,thr1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thr2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thr3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thr4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thr5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('BINARY',thr1)
cv2.imshow('BINARY_INV',thr2)
cv2.imshow('TRUNC',thr3)
cv2.imshow('TOZERO',thr4)
cv2.imshow('TOZERO_INV',thr5)


cv2.waitKey(0)
cv2.destroyAllWindows()

print("Alan Romero NC = 0124")