
import cv2
import os
 
 # Use VideoCapture para capturar video, aquí usamos video local
cap = cv2.VideoCapture("normal_1.mp4")
 
 # Crea un archivo para guardar el fotograma del video
save_path = os.makedirs("normal")
 
 # Nombra la captura de pantalla de la imagen
imgPath = ""
 
 # Número total de fotogramas de video
sum = cap.get(7)
 
 # De punto flotante a entero, calcula el intervalo de fotogramas interceptados, aquí interceptará 30 imágenes
time = (int)(sum / 80)
 # Restablecer el número total de fotogramas de video
sum = 0
 # El número de imágenes a interceptar
i = 0
 
while True:
	ret, frame = cap.read()
         # Leer fotograma de video
	if ret == False:
		break
	sum += 1
	if sum % time == 0 and i < 1000:
		i += 1
                 # Usa i para nombrar la imagen
		imgPath = "normal/4%s.jpg" % str(i)
                 # Almacene el fotograma de video extraído en imgPath
		cv2.imwrite(imgPath, frame)
 
print("¡terminar!") #La extracción ha terminado, finaliza la impresión