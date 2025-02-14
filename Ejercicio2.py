import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar imagen en escala de grises
image = cv2.imread('cubo.jpg', cv2.IMREAD_GRAYSCALE)

# Detección de bordes con Canny
edges = cv2.Canny(image, 50, 150)

# Aplicación de la Transformada de Hough para líneas
lines = cv2.HoughLines(edges, rho=1, theta=np.pi/180, threshold=100)

# Crear una copia de la imagen original para dibujar las líneas
output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(output_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Mostrar la imagen con las líneas detectadas
plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
plt.title("Líneas detectadas")
plt.show()
