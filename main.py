from turtle import Turtle, Screen
import random
import turtle

# timmy.color("blue")

# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pend

# num_sides = 5

# def draw_shape(num_sides):
#     angle = 360 / num_sides 
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
    


turtle.colormode(255)
timmy = Turtle()
timmy.speed("fastest")

def change_color():
    R = random.randint(0, 255)
    B = random.randint(0, 255)
    G = random.randint(0, 255)
    color = (R, G, B)
    return color


for _ in range(36):
    current_heading = timmy.heading()
    timmy.setheading(current_heading + 10)
    timmy.color(change_color())
    timmy.circle(100)



screen = Screen()
screen.exitonclick()
# for shape_side in range(3, 11):
#     draw_shape(shape_side)
#     change_color()

# def random_walk(num_steps):
#     directions = [0, 90, 180, 270]
#     for _ in range(num_steps):
#         timmy.setheading(random.choice(directions))
#         timmy.forward(30)
#         change_color()

# random_walk(200)

