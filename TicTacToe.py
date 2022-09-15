"""
Juego Tic Tac Toe A01709338 Version 3
De ser aplicado, este commit enviará un mensaje a los jugadores cada vez que un cuadro haya sido ocupado.
"""

from freegames import line
from turtle import *
import freegames
"Se importan las librerías de turtle graphics y freegames "


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
    "Avisar que el cuadro ha sido ocupado una vez que se dibuja la figura."
    textinput("Cuadro ocupado.", "Inténtelo de nuevo.")


"Dimensiones de la cuadrícula."
setup(450, 450, 320, 50)

"Oculta la tortuga de la paquetería de gráficos"
hideturtle()

"Acelerar la animación de los dibujos y delay."
tracer(False)

"Funciones de turtle graphics para la cuadrícula"
grid()

"Función para refrescar la animación o dibujo. "
update()

"Función para activar el programa al dar click en pantalla"
onscreenclick(tap)
done()