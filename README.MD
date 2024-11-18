# Detección de Líneas con la Transformada de Hough

Este proyecto utiliza la **Transformada de Hough** para detectar líneas rectas en una imagen. Se emplean bibliotecas como **OpenCV**, **NumPy** y **Matplotlib** para procesar imágenes y mostrar los resultados.

---

## **Descripción**

El script realiza las siguientes tareas:

1. **Carga de una imagen**: La imagen se carga en escala de grises para simplificar el procesamiento.
2. **Detección de bordes**: Utiliza el algoritmo de Canny para detectar bordes relevantes en la imagen.
3. **Transformada de Hough**: Aplica la Transformada de Hough para identificar líneas rectas en los bordes detectados.
4. **Dibujo de líneas**: Superpone las líneas detectadas sobre la imagen original.
5. **Visualización de resultados**: Muestra la imagen con las líneas detectadas utilizando Matplotlib.

---

## **Requisitos**

Antes de ejecutar el código, asegúrate de tener instaladas las siguientes dependencias:

- **Python 3.7 o superior**
- **OpenCV**: Biblioteca para procesamiento de imágenes.
- **NumPy**: Para cálculos matriciales.
- **Matplotlib**: Para mostrar los resultados.

### **Instalación de dependencias**

Ejecuta el siguiente comando para instalar las bibliotecas necesarias:

```bash
pip install opencv-python matplotlib numpy
```
