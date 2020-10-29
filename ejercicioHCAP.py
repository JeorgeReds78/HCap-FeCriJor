import cv2
import numpy as np

#Función de la escala de grises
def escala_gris(A):
    B = np.zeros([A.shape[0], A.shape[1]])
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            suma = 0
            for k in range(0, len(A[0][0])):
                suma += A[i][j][k]
            suma = int(suma/len(A[0][0]))
            B[i][j] = suma
    return B

#Función de la convolucio
def convolucion(A, B):
    C = np.zeros([A.shape[0]-2, A.shape[1]-2])
    for i in range(0, len(A)-2):
        for j in range(0, len(A[0])-2):
            suma = 0
            for x in range(0, len(B)):
                for y in range(0, len(B[0])):
                    suma += A[i+x][j+y]*B[x][y]
            if suma > 255:
                suma = 255
            C[i][j] = suma
    return C

#Función de la escala en blanco y negro
def escala_BN(A):
    B = np.zeros([A.shape[0], A.shape[1]])
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            if A[i][j] > 128:
                B[i][j] = 255
    return B

#Función para agregar 0
def padding(A):
    B = np.zeros((len(A)+2, len(A[0])+2))
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            B[i+1][j+1] = A[i][j]
    return B

Filtro = [[1, 1, 1],[1, 0, 1],[1, 1, 1]]
Img = cv2.imread('image.jpg')
Img = cv2.cvtColor(Img,cv2.COLOR_BGR2RGB)

Img2 = escala_gris(Img)
cv2.imwrite('gris.jpg', Img2)

Img_pad = padding(Img2)
Img_pad = convolucion(Img_pad, Filtro)
cv2.imwrite('pad.jpg', Img_pad)

Img_sin_pad = convolucion(Img2, Filtro)
cv2.imwrite('sinpad.jpg', Img_sin_pad)

Img_BN = escala_BN(Img2)
cv2.imwrite('blancoYNegro.jpg', Img_BN)

