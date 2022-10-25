from turtle import *;

pen = Turtle();

def move_forward():
    pen.forward(10);

def move_backward():
    pen.backward(10);
    
def turn_left():
    pen.left(10);
    
def turn_right():
    pen.right(10);

def clear_screen():
    pen.clear();
    pen.hideturtle();
    pen.up();
    pen.goto(0, 0);
    pen.down();
    pen.showturtle();