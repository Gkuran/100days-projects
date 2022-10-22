from turtle import *;
from misc import *;

for i in range(3, 50):
    r_colour = choice(colours);
    my_turtle.pencolor(r_colour);
    for j in range(i):
        my_turtle.forward(100/2);
        my_turtle.right(360/i)

screen = Screen();
screen.exitonclick();