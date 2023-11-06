import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.goto(0, 0)
pen.pendown()

# Function to draw a mandala-like pattern
def draw_mandala():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for _ in range(72):
        pen.color(random.choice(colors))
        for _ in range(6):
            pen.forward(100)
            pen.right(60)
        pen.right(5)

# Draw the mandala-like pattern
draw_mandala()

# Hide the turtle
pen.hideturtle()

# Close the window on click
screen.exitonclick()