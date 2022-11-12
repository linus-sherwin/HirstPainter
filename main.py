import turtle as t
import random

painter = t.Turtle()
painter.shape("turtle")
painter.speed("fastest")
painter.penup()
painter.hideturtle()
# Color palette from the original Damien Hirst Painting
color_list = [(237, 245, 240), (212, 149, 95), (215, 80, 62), (47, 94, 142),
              (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15),
              (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183),
              (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196),
              (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220)]
t.colormode(255)
painter.setheading(222.5)
painter.forward(450)
painter.setheading(0)
number_of_dots = 196

for dot_count in range(1, number_of_dots + 1):
    painter.dot(20, random.choice(color_list))
    painter.forward(50)
    if dot_count % 14 == 0:
        painter.setheading(90)
        painter.forward(50)
        painter.setheading(180)
        painter.forward(700)
        painter.setheading(0)

screen = t.Screen()
screen.exitonclick()
