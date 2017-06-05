import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.penup()

t.setx(-40)
t.sety(-40)

t.pendown()

for i in range(4) :
    t.forward(80)
    t.left(90)

t.forward(120)

t.left(90)

t.forward(200)

t.left(90)

t.forward(160)

t.left(90)

t.forward(200)

t.left(90)

t.forward(40)

t.penup()

t.setx(-80)
t.sety(160)

t.pendown()

t.left(45)

t.forward(160*(1/1.414))

t.right(90)

t.forward(160*(1/1.414))

t.penup()

t.setx(-40)
t.sety(120)

t.pendown()

t.dot(30)

t.penup()

t.setx(40)
t.sety(120)

t.pendown()

t.dot(30)
