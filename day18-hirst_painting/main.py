from getColour import *;
from turtle import *;
import random;

pen = Turtle();
pen.speed("fastest");
screen = Screen();
screen.colormode(255);

pen.hideturtle();
pen.up();

x = -230;
y = -230;
pen.goto(x, y);

for _ in range(10):
    y += 40;
    pen.goto(x, y);
    for _ in range(10):
        random_colour = random.choice(rgb_colours);
        pen.down();
        pen.dot(20, random_colour);
        pen.up();
        pen.forward(50);

screen.exitonclick();