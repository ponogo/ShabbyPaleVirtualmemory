import turtle

turtle.title("My Turtle Game")
turtle.bgcolor("purple")
turtle.setup(600,600)

screen = turtle.Screen()
bob = turtle.Turtle()
bob.shape("turtle")
bob.color("yellow")

def pattern():
  for i in range(36):
    bob.circle(100)
    bob.right(10)

screen.onkey(pattern, "space")
screen.onclick(bob.goto)
screen.listen()


print("click on turtle then press space to start pattern")