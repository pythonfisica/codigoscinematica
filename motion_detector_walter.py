# -*- coding: utf-8 -*-

import imutils

import cv2

import numpy as np

import matplotlib.pyplot as plt

#
camera = cv2.VideoCapture(".\cohete.mp4")

# Crear MOG ventana para observar el video
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
# Iniciar la primera capa del video
firstFrame = None
# Loop por todas las capas del video
while True:
	(grabbed, frame) = camera.read()
	text = "desocupado"
	if not grabbed:
		break
	# cambiar el tamaño del marco, convertirlo en escala de grises y difuminarlo
	frame = imutils.resize(frame, width=400)
	frame_height = np.shape(frame)[0]
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (25, 25), 0)
#	Si el primer cuadro es Ninguno, inicialízalo.
	if firstFrame is None:
		firstFrame = gray
		continue
# calcular la diferencia absoluta entre el cuadro actual y
# primer cuadro
	frameDelta = cv2.absdiff(firstFrame, gray)

	thresh = fgbg.apply(frame)
# dilate la imagen del umbral para rellenar los agujeros, luego encuentra los contornos
# en la imagen del umbral
	thresh = cv2.dilate(thresh, None, iterations=2)
#
	(_,cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
 	# bucle sobre los contornos
	px=[]
	py=[]
	for c in cnts:
		# si el contorno es demasiado pequeño, ignóralo
		if cv2.contourArea(c) < 500:
			continue

		# calcular el cuadro delimitador para el contorno, dibujarlo en el marco,
        # y actualizar el texto
		(x, y, w, h) = cv2.boundingRect(c)

		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)

# muestra el marco 
	cv2.imshow("Detector Movimiento", frame)
	plt.pause(0.5)

	key = cv2.waitKey(1) & 0xFF
 
	# si se presiona la tecla `q`, salte del loop
	plt.pause(0.01)
	if key == ord("q"):
		break
fourcc = cv2.VideoWriter_fourcc(*'MSVC')
out = cv2.VideoWriter('seguidor_cohete.avi',fourcc, 25.0, (640,480))

while(camera.isOpened()):
    ret, frame = camera.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # escribe el marco volteado
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# limpia la cámara y cierra cualquier ventana abierta
out.release()
camera.release()
cv2.destroyAllWindows()

