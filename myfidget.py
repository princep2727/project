#my fidget spinner
from turtle import *
state ={'turn': 100}

def spinner():
    "draw fidget spinner"
    clear()
    angle = state['turn']/10
    right(angle)
    forward(100)
    dot(120,'red')
    back(100)
    right(120)
    forward(100)
    dot(120,'green')
    back(100)
    right(120)
    forward(100)
    dot(120,'blue')
    back(100)
    right(120)
    update()

def animate():
    "animate fidget spinner"
    if state['turn'] > 0:
        state['turn'] -= 1

    spinner()
    ontimer(animate, 20)

def flick():
    "Flick fidget spinner."
    #print("input speed on flick",state['turn'] )
    state['turn'] += int(input(""))

setup(450,450,390,10)
hideturtle()
tracer(False)
width(20)
onkey(flick,'space')
listen()
animate()
done()