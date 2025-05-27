import turtle

# Set up turtle screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Heart Drawing")

# Create turtle object
pen = turtle.Turtle()
pen.color("red")
pen.pensize(3)
pen.speed(1)

# Start drawing heart
pen.begin_fill()

pen.left(50)
pen.forward(133)
pen.circle(50, 200)
pen.right(140)
pen.circle(50, 200)
pen.forward(133)

pen.end_fill()

# Hide turtle
pen.hideturtle()

# Keep the window open
turtle.done()
