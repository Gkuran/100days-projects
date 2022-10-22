from turtle import *;
from misc import *;

screen = Screen();
screen.colormode(255);

my_turtle.speed("fastest");


for i in range(0, 359):
    headingAngle = my_turtle.heading();
    colour = randomHex();
    my_turtle.color(colour);
    my_turtle.circle(100);
    my_turtle.setheading(headingAngle + 10);

screen.exitonclick();