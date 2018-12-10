# -*- coding: utf-8 -*-
"""
Funcion para resolver Ecuaciones de segundo Grado

@author: Walter
"""

from math import sqrt #raiz cuadrada

def Ec_Cuadrada():
    print("\n Este programa permite encontrar las raices de un ecuación cuadrada")
    a = float(input("Ingrese el primer coeficiente: "))
    b = float(input("Ingrese el segundo coeficiente: "))
    c = float(input("Ingrese el tercer coeficiente: "))
    disc = b**2 - 4*a*c #discriminante b^2 - 4ac
    if disc > 0:
        valor_disc = sqrt(disc)
        positivo = (-b + valor_disc) / (2*a)
        negativo = (-b - valor_disc) / (2*a)
        print("Los valores de las raices son: "+str(round(positivo,2))+" y " +str(round(negativo,2)))
    elif disc == 0:
        valor_disc = sqrt(disc)
        positivo = (-b + valor_disc) / (2*a)
        print("La raíz de la ecuacion cuadrática es: "+str(positivo))
    else:
        print("La ecuación no tiene solución en los números reales")
    
    

Ec_Cuadrada()

