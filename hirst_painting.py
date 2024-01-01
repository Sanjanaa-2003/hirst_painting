import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124),
              (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86),
              (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158),
              (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90),
              (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153),
              (174, 94, 97), (176, 192, 209)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):      #iterates 100 times for 100 dots
    tim.dot(20, random.choice(color_list))  #each dot has a random color
    tim.forward(50) #distance between each dot

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


# From turtle we need to import the Turtle, Screen, and colormode
# And we require the random module.
# #We need to define the colormode of our Turtle so that we can use the RGB with no error.
# colormode(255)
# Then we will create an object of the Turtle Class.
# t1 = Turtle()
# After that we will create an array that will contain all the colors RGB tuples that we want in the painting.
# Then we will set the speed of the turtle to 0 i.e. fastest speed along with this we will setheading to 255 which will make the turtle turn 255 degrees.
# t1.speed(0)
# t1.setheading(225)
# We will call the penup function from the turtle class this function will help us not draw a line on the screen when we move from one place to another.
# t1.penup()
# Then we will hide the turtle from the screen.
# t1.hideturtle()
# Then we will move the turtle forward by 350.
# t1.forward(350)
# Now we will set the heading again to 0 degrees which are in its original direction.
# t1.setheading(0)
# Create a function hirst_ that will take the number of dots we want in our painting as input.
# In this function we will traverse from 1 to the number of dots entered by the user and print the dot and move forward. If we reach the number that is divisible by 10 then we will go up by 50 and set the heading to the left side i.e. 180 degrees and move 500 and then set the heading to 0 and then start again from there.
# Then we will call the hirst_() function to draw the hirst dot painting.
# After that we will create an object of class Screen and call the exitonclick() function that will stop the tkinter screen from closing itself after creating the painting.