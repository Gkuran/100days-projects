from controls import *;
from turtle import *;

screen = Screen();
screen.listen();

screen.onkey(key="w", fun=move_forward);
screen.onkey(key="s", fun=move_backward);
screen.onkey(key="a", fun=turn_left);
screen.onkey(key="d", fun=turn_right);
screen.onkey(key="c", fun=clear_screen);

screen.exitonclick(); 