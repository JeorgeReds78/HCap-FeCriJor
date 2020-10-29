import cv2
import numpy as np

#Función de la escala de grises
def escala_gris(A):
    B = np.zeros(A.shape)
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            suma = 0
            for k in range(0, len(A[0][0])):
                suma += A[i][j][k]
            suma = int(suma/len(A[0][0]))
            B[i][j] = suma
    return B

#Función de la convolucion con padding
def convolucion_padding(A, B):
    C = np.zeros(len(A), len(A[0]))
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            suma = 0
            for x in range(0, len(B)):
                for y in range(0, len(B[0])):
                    suma += A[i+x][j+y]*B[x][y]
            C[i][j] = suma
    return C

#Función de la convolucion sin padding
def convolucion_sin_padding(A, B):
    C = np.zeros((len(A)-2, len(A[0])-2))
    for i in range(0, len(A)-2):
        for j in range(0, len(A[0])-2):
            suma = 0
            for x in range(0, len(B)):
                for y in range(0, len(B[0])):
                    suma += A[i+x][j+y]*B[x][y]
            C[i][j] = suma
    return C

#Función de la escala en blanco y negro
def escala_BN(A):
    B = np.zeros(len(A), len(A[0]))
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            if A[i][j] > 128:
                B[i][j] = 1
    return B

#Función para agregar 0
def padding(A):
    B = np.zeros((len(A)+2, len(A[0])+2))
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            B[i+1][j+1] = A[i][j]
    return B

Matriz = [[1, 1], [1, 1]]
Filtro = [[3, 4, 2],[1, 0, 1],[2, 3, 1]]
Img = cv2.imread('image.jpg')
Img = cv2.cvtColor(Img,cv2.COLOR_BGR2RGB)

Img2 = escala_gris(Img)
print(Img2)
cv2.imwrite('gris.jpg', Img2)

