"""Juego Tic Tac Toe A01709338 Version 2
En este commit se comenta el código y se agregan librerías.

"""

"Se importan las librerías de turtle graphics y freegames "
import freegames
from turtle import * 

from freegames import line 

"Dibujar la tabla de juego compuesta de 9 cuadros."
def grid():

    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

"Dibujar el jugador de x"
def drawx(x, y):
    
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)


def drawo(x, y):
    "Dibujar el jugador de O"
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)


def floor(value):
    "Valor de círculo O en los cuadros con valor de 133"
    return ((value + 200) // 133) * 133 - 200

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
setup(420, 420, 370, 0)
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