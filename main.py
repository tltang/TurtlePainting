# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# import turtle
# from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)

clifford = t.Turtle()

clifford.shape("square")
clifford.color("green")
# “fastest”: 0
# “fast”: 10
# “normal”: 6
# “slow”: 3
# “slowest”: 1
clifford.speed(10)
colors = ["lime green", "red", "blue", "purple", "orange", "yellow"]
angles = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

#spiralcircle
def draw_spiragraph(gap):
    for _ in range(int(360 / gap)):
        color = random_color()
        clifford.color(color)
        # clifford.right(angle)
        clifford.circle(100)
        current_heading = clifford.heading() + gap
        clifford.setheading(current_heading)

draw_spiragraph(5)

# #random walk
# clifford.shapesize(0.5)
# clifford.pensize(width=10)
# clifford.width(width=10)
# for _ in range(1000):
#     angle = random.choice(angles)
#     color = random_color()
#     clifford.color(color)
#     clifford.setheading(angle)
#     # clifford.right(angle)
#     clifford.forward(20)

# # shapes with random color
# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         clifford.forward(100)
#         clifford.right(angle)
#
# for i in range(3, 11):
#     clifford.color(random.choice(colors))
#     draw_shape(i)


# #square
# for i in range(4):
#     clifford.right(90)
#     clifford.forward(90)

# #dashline
# for i in range(20):
#     clifford.forward(10)
#     clifford.penup()
#     clifford.forward(10)
#     clifford.pendown()

# #import prettytable
# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
#
# print(table)

my_screen = t.Screen()
my_screen.exitonclick()
