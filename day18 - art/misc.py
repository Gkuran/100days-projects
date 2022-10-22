from secrets import choice
from turtle import *;
import random;

# Setting up the initial position on canvas:
my_turtle = Turtle();

my_start = (-50, 100);
my_turtle.penup();
my_turtle.setx(my_start[0]);
my_turtle.sety(my_start[1]);
my_turtle.pendown();

# Generating random hex colours:
def randomHex():    
    r = random.randint(0, 255);
    g = random.randint(0, 255);
    b = random.randint(0, 255);
    return (r, g, b);

# Colour list:
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"];

# Random Walk:
angle_list = [90, 180, 270, 360];
# def RandomAngle():
#    return random.randint(0, 359);
