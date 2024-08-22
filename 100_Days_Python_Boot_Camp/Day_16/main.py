# import another_module
#
# print(another_module.another_variable)

# Class is denoted by Pascal case name eg: Turtle class inside turtle module

# import turtle
#
# timmy = turtle.Turtle()

from turtle import Turtle, Screen

timmy = Turtle()

print(timmy)  # Object is being printed <turtle.Turtle object at 0x000001C29E6554D0>
timmy.shape("turtle")
timmy.color("DeepPink")
timmy.forward(100)


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

