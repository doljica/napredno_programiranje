import turtle

wn = turtle.Screen()
wn.title("Pong by DO")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) # sprječava da se prozor updatea, omogućava da se ubrza igrica

# Score
score_a = 0
score_b = 0

# Reket A
reket_a = turtle.Turtle()  # malo "t" je modul, veliko "t" je klasa
reket_a.speed(0)  # brzina animacije
reket_a.shape("square")
reket_a.color("white")
reket_a.shapesize(stretch_wid=5, stretch_len=1)
reket_a.penup() # nema traga crte koju ostavlja turtle modul
reket_a.goto(-350, 0)

# Reket B
reket_b = turtle.Turtle()  
reket_b.speed(0)  
reket_b.shape("square")
reket_b.color("white")
reket_b.shapesize(stretch_wid=5, stretch_len=1)
reket_b.penup() 
reket_b.goto(350, 0)

# Lopta
lopta = turtle.Turtle()  
lopta.speed(0)  
lopta.shape("square")
lopta.color("white")
lopta.penup() 
lopta.goto(0, 0)
lopta.dx = 0.1
lopta.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Funkcije
def reket_a_gore():
    y = reket_a.ycor()
    y +=20
    reket_a.sety(y)


def reket_a_dolje():
    y = reket_a.ycor()
    y -=20
    reket_a.sety(y)


def reket_b_gore():
    y = reket_b.ycor()
    y +=20
    reket_b.sety(y)


def reket_b_dolje():
    y = reket_b.ycor()
    y -=20
    reket_b.sety(y)


# Povezivanje tipkovnice
wn.listen()
wn.onkeypress(reket_a_gore, "w")
wn.onkeypress(reket_a_dolje, "s")
wn.onkeypress(reket_b_gore, "Up")
wn.onkeypress(reket_b_dolje, "Down")

# Main game loop
while True:
    wn.update() # svaki put kad se loop pokrene, updatea se screen


    # Miči loptu
    lopta.setx(lopta.xcor() + lopta.dx)
    lopta.sety(lopta.ycor() + lopta.dy)

    # Granice
    if lopta.ycor() > 290:
        lopta.sety(290)
        lopta.dy *= -1

    if lopta.ycor() < -290:
        lopta.sety(-290)
        lopta.dy *= -1


    if lopta.xcor() > 390:
        lopta.goto(0, 0)
        lopta.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if lopta.xcor() < -390:
        lopta.goto(0, 0)
        lopta.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    # Sudar reketa i lopte
    if (lopta.xcor() > 340 and lopta.xcor() < 350) and (lopta.ycor() < reket_b.ycor() + 40 and lopta.ycor() > reket_b.ycor() -40):
        lopta.setx(340)
        lopta.dx *= -1


    if (lopta.xcor() < -340 and lopta.xcor() > -350) and (lopta.ycor() < reket_a.ycor() + 40 and lopta.ycor() > reket_a.ycor() -40):
        lopta.setx(-340)
        lopta.dx *= -1




