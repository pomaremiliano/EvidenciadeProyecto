"""
Juego Tic Tac Toe A01709338 Version 3
En este commit se modifica el tamaño, color, y centrado de los símbolos X y O
"""

"Se importan las librerías de turtle graphics y freegames "
import freegames
from turtle import * 

from freegames import line 

"Dibujar la tabla de juego compuesta de 9 cuadros."
def grid():

    line(-65, 200, -65, -200)
    line(65, 200, 65, -200)
    line(-200, -65, 200, -65)
    line(-200, 65, 200, 65)

"Dibujar el jugador de x en color azul"
def drawx(x, y):
    color("blue")
    line(x, y, x + 130, y + 130)
    color("blue") 
    line(x, y + 130, x + 130, y)
    color("blue")


def drawo(x, y):
    "Dibujar el jugador de O en color azul"
    up()
    goto(x + 65, y + 25)
    down()
    circle(40)
    


def floor(value):
    "Valor de círculo O en los cuadros con valor de 133"
    return ((value + 200) // 135) * 135 - 200

"Estatus de jugador al ejecutar y lista de jugadores X y O"
state = {'player': 0}
players = [drawx, drawo]


"Dibujar X y O en el cuadro seleccionado"
def tap(x, y):
    
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


"Dimensiones"
setup(450, 450, 320, 50)
"Turtle graphics"
hideturtle()
"Rastrear ejecución de turtle graphics"
tracer(False)
"Funciones de turtle graphics para la cuadrícula"
grid()
"Funcion para click en pantalla"
update()
onscreenclick(tap)
done()
