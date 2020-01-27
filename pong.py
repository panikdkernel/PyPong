# simple pong in python 3 
# from youtube freecodecamp

import turtle

window = turtle.Screen()
window.title("pyPong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Main game loop
while True:
    window.update()
