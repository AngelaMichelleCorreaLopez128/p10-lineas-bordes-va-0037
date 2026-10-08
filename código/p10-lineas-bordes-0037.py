# Angela Correa NC = 0037
print("EJEMPLO 1 — Detección de líneas")
print("+--++++-+-++--+-+-++--++--+-++-+-")
import cv2
import numpy as np

# Cargar imagen
imagen = cv2.imread("lineas_esquinas_jaguar.jpg")

# Verificar que la imagen exista
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
    exit()

# 1. Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# 2. Detectar bordes
bordes = cv2.Canny(gris, 50, 150)

# 3. Detectar líneas mediante Hough
lineas = cv2.HoughLinesP(
    bordes,
    1,
    np.pi / 180,
    threshold=50,
    minLineLength=50,
    maxLineGap=10
)

# Crear copia de la imagen original
resultado = imagen.copy()

# 4. Dibujar líneas detectadas
if lineas is not None:

    for linea in lineas:

        x1, y1, x2, y2 = linea.flatten()

        cv2.line(
            resultado,
            (x1, y1),
            (x2, y2),
            (0, 0, 255),
            2
        )

# 5. Mostrar las 3 imágenes

cv2.imshow("1 - Imagen original 0037", imagen)

cv2.imshow("2 - Bordes 0037", bordes)

cv2.imshow("3 - Lineas detectadas 0037", resultado)

# 6. Guardar resultado
cv2.imwrite(
    "../resultados/ejemplo1_lineas.jpg",
    resultado
)

# Mostrar información
print("Deteccion de lineas terminada.")

if lineas is not None:
    print("Cantidad de segmentos detectados:", len(lineas))
else:
    print("No se detectaron lineas.")

print("Resultado guardado en:")
print("../resultados/ejemplo1_lineas.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar las tres ventanas
cv2.destroyAllWindows()
print("Angela Correa NC = 0037")