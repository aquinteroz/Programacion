# DrawTreeDynamic.py
'''Dibuja un árbol'''

import turtle
import random

def dibujar_arbol(longitud, disminucion, angulo, ruido = 0):
    if longitud < 10:
        return
        
    turtle.width(longitud/12)
    turtle.forward(longitud)
    cambio_longitud = longitud * disminucion
    
    if ruido:
        cambio_longitud *= random.uniform(0.9,1.1)
        
    angulo_derecho = angulo + random.gauss(0, ruido)
    angulo_izquierdo = angulo + random.gauss(0, ruido)
    
    turtle.left(angulo_izquierdo)
    dibujar_arbol(cambio_longitud, disminucion, angulo, ruido)
    turtle.right(angulo_izquierdo)
    
    turtle.right(angulo_derecho)
    dibujar_arbol(cambio_longitud, disminucion, angulo, ruido)
    turtle.left(angulo_derecho)
    
    turtle.backward(longitud)
    
turtle.bgcolor('#D6D2C4')
turtle.pencolor('#D3273E')
turtle.penup()
turtle.goto(0,-300)
turtle.pendown()
turtle.left(90)
turtle.speed(0)
dibujar_arbol(130,0.8,18,8)
turtle.done()