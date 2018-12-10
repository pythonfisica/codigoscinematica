# -*- coding: utf-8 -*-
"""
@author: Walter
"""
"""
Gráfica del problema 2 en base a la ecuacion itinerario presente en la página 52 del Texto del Estudiante de Física 2018.
"""
import numpy as np
import matplotlib.pyplot as plt

#Valores del tiempo
t = np.arange(0., 10.,.2) #valor inicial, valor final,saltos entre valor
#Funcion Cuadrática
x = 3 + 5*t + 2*(t**2)

plt.figure()
#Graficar funciones
plt.plot(t, x, "go-")

#Linea comience en el 0,0
plt.xlim(0)
plt.ylim(0)

#Titulo
plt.title("Gráfico MRUA")

#nombre ejes
plt.xlabel("Tiempo [s]")
plt.ylabel("Posicion[m]")
#Grilla
plt.grid()
#Guardar imagen
plt.savefig("Grafico funcion.png")
#mostrar grafico
plt.show()