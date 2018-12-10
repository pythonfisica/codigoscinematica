# -*- coding: utf-8 -*-
"""

@author: Walter
"""
"""
Creacion de gráfico en base a la tabla itinerario,
mediante el uso de contenedores tipos lista,
presente en la página 41 del Texto del Estudiante de Física 2018.
"""
#import numpy as np #libreria util para calculos matematicos (http://www.numpy.org/)
import matplotlib.pyplot as plt #libreria util para realizar graficos (https://matplotlib.org/gallery.html)
import webbrowser #abrir archivos desde directorio

#Tabla Itinerario

tiempo = [0,1,2,3]#listas
posicion = [0,5,10,15]#listas

#Grafica de la tabla
fig = plt.figure() #construccion figura
ax = fig.add_subplot(111) #construccion subplot
xs = tiempo #eje x
ys = posicion #eje y
#Titulo del grafico
plt.title("Gráfico Posición vs Tiempo \n Movimiento Rectilíneo Uniforme")
#Construccion grafico
ax.plot(xs, ys)
#Limite de los ejes
ax.set_ylim(ymin=0)
ax.set_xlim(xmin=0)
#Nombre de los ejes
plt.ylabel("Posicion [m]")
plt.xlabel("Tiempo[s]")
#Guardar Imagen
plt.savefig("Grafico MRU-lista.png")
#abrir imagen
plt.show()
#abrir imagen desde archivo
webbrowser.open("Grafico MRU-lista.png")


