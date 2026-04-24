import turtle
import math
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Defender")
screen.setup(width=600, height=600)
screen.tracer(0)

# Score
score = 0

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.forward(600)
    border_pen.left(90)
border_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 20

# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("square")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 5
bulletstate = "ready"

# Create the enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
x = random.randint(-280, 280)
y = 280
enemy.setposition(x, y)

enemyspeed = 1

# Score display
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 270)
scorestring = f"Score: {score}"
score_pen.write(scorestring, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 20:
        return True
    else:
        return False

# Keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(fire_bullet, "space")

# Main game loop
while True:
    screen.update()

    # Move the enemy
    y = enemy.ycor()
    y -= enemyspeed
    enemy.sety(y)

    # Check if enemy reached the bottom
    if enemy.ycor() < -290:
        # Reset enemy
        x = random.randint(-280, 280)
        enemy.setposition(x, 280)
        # Decrease score or reset
        score -= 5
        score_pen.clear()
        score_pen.write(f"Score: {score}", align="left", font=("Arial", 14, "normal"))

    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Check if bullet reached the top
    if bullet.ycor() > 290:
        bullet.hideturtle()
        bulletstate = "ready"

    # Check for collision between bullet and enemy
    if is_collision(bullet, enemy):
        # Reset the bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        # Reset the enemy
        x = random.randint(-280, 280)
        enemy.setposition(x, 280)
        # Update the score
        score += 10
        score_pen.clear()
        score_pen.write(f"Score: {score}", align="left", font=("Arial", 14, "normal"))
    
    # Check for collision between player and enemy
    if is_collision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("GAME OVER")
        break

# Game Over Screen
score_pen.setposition(0, 0)
score_pen.write("GAME OVER", align="center", font=("Arial", 30, "bold"))
screen.update()

turtle.done()
