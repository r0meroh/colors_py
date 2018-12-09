import random
from turtle import *
import graphics

# create turtle object
t1 = Turtle()
# speed object is drawn
t1.speed(2)
# pen up
t1.pu()


# string of colors
colors = ["blue", "red", "green", "yellow", "purple", "orange"]


# circle_size = (50,59)
while True:
    circle_color = random.choice(colors)
# cursor navigation
    # t1.goto(100,100)
    t1.goto(random.randint(0,300), random.randint(0,300))
# initiate drawing
    t1.down()
# fill color in
    t1.begin_fill()
    t1.color(circle_color)
    t1.speed(30)
    t1.circle(20,360)
    t1.end_fill()
# lift pen to finish drawing
    t1.up()
# window waits for user to exit
done()
