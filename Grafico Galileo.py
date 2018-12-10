# -*- coding: utf-8 -*-
"""
@author: Walter
""" """
Creacion de gráfico en base a la tabla itinerario presente en la página 59 del Texto del Estudiante de Física 2018.
"""

import matplotlib.pyplot as plt #libreria util para realizar graficos 
#(https://matplotlib.org/gallery.html) (https://matplotlib.org/users/pyplot_tutorial.html)
import webbrowser #abrir archivo una vez compilado el codigo
import numpy as np #libreria numpy, util para realizar operaciones matemáticas (http://www.numpy.org/)

#Tabla Itinerario
tiempo = [0,1,2,3,4,5]
posicion = [0,25,100,225,400,625]
tiempo_array = np.array(tiempo) #transformamos la lista en un tipo de objeto (array) que permite realizar operaciones matematicas
tiempo_cuadrado = tiempo_array**2

#Grafica de la tabla
fig = plt.figure(figsize=(10,8))
ax1 = plt.subplot(121)
xs_1 = tiempo
ys_1 = posicion
plt.title("Gráfico Posición vs Tiempo \n Experimento Galileo")
ax1.plot(xs_1, ys_1,"ro-")#ro- en el gráfico se representan los puntos, se unen por lineas continuas de color rojo.
ax1.set_ylim(ymin=0)
ax1.set_xlim(xmin=0)
plt.ylabel("Posicion [m]")
plt.xlabel("Tiempo[s]")

ax2 = plt.subplot(122)
xs_2 = tiempo_cuadrado
ys_2 = posicion
plt.title("Gráfico Posición vs Tiempo al cuadrado \n Experimento Galileo")
ax2.plot(xs_2, ys_2,"bo-")#ro- en el gráfico se representan los puntos, se unen por lineas continuas de color azul.
ax2.set_ylim(ymin=0)
ax2.set_xlim(xmin=0)
plt.ylabel("Posicion [m]")
plt.xlabel("Tiempo al cuadrado[s^2]")

plt.savefig("Grafico Galileo.png")

fig.show()

webbrowser.open("Grafico Galileo.png")


