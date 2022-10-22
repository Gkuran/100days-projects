from turtle import *;
from misc import *;

STEPS = 1000;
STEPLENGTH = 20;
SPEED = "fastest";
SIZE = 15;

my_turtle.speed(SPEED);
my_turtle.pensize(SIZE);

screen = Screen();
screen.colormode(255)

for _ in range(STEPS):
    #random_angle = RandomAngle();
    screen.colormode(255)
    random_angle = choice(angle_list);
    colour = randomHex();
    my_turtle.color(colour);
    my_turtle.forward(STEPLENGTH);
    my_turtle.setheading(random_angle);
    
screen.exitonclick();