import turtle
import math
import random

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("background3.gif")

#Register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

#Pen Setup for Border
border_pen = turtle.Turtle() #Creating the turtle
border_pen.speed(0) #Turtle Speed - fast
border_pen.color("white") #Turtle Color

#To Draw Border
border_pen.penup() #lifts pen up to start drawing border
border_pen.setposition(-300,-300) #initial position
border_pen.pendown() #places pen down
border_pen.pensize(3) #sets pen size
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Set the score to 0
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 270)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()



#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player .gif")
#Positioning it
player.penup() #to prevent drawing in the background by lifting up pen
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#Move the player left and right
def move_left():
    x = player.xcor() #xcor represents the position function of the player
    x -= playerspeed
    #sets a limit that stops the player from moving past the borders
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    player.setx(x)
    #sets a limit that stops the player from moving past the borders
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #declare bullet as a global if it needs changed, where if we change it in the function, it changes outside too
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x, y + 10)
        bullet.showturtle()

def isCollision(d1, d2):
    distance = math.sqrt((math.pow((d1.xcor() - d2.xcor()), 2)) + (math.pow((d1.ycor() - d2.ycor()), 2)))
    if distance < 15:
        return True
    else:
        return False

#Choose a number of enemies
number_of_enemies = 10
#Create an empty list of enemies
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
    #Create the enemies
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed("fastest")
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2

#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
#bullet is hidden at the start of the game
bullet.hideturtle()

bulletspeed = 20

#Define bullet state
#ready state - ready to fire
#fire state - bullet is fired
bulletstate = "ready"


#Create keyboard bindings
turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(fire_bullet, "space")

#Main game loop
while True:

    for enemy in enemies:
        #Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #Move enemy back and down
        if enemy.xcor() > 280:
            #Moves all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Change enemy direction
            enemyspeed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        #Check for a collision between the bullet and the enemy
        if isCollision(bullet, enemy):
            #Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400) #moves bullet off screen so enemies won't run into it
            #Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(200, 250)
            enemy.setposition(x, y)
            #Update score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))


        if isCollision(enemy, player):
            enemy.hideturtle()
            player.hideturtle()
            #Game Over Message
            gm = turtle.Turtle()
            gm.speed(0)
            gm.color("white")
            gm.penup()
            gm.setposition(0, 0)
            scorestring = "\"Close But Not Close Enough\""
            gm.write(scorestring, False, align="center", font=("Arial", 30, "normal"))
            gm.hideturtle()
            #print("Game Over")
            break

    #Move bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Check to see if bullet has gone to the top so the function can reset to ready
    if bullet.ycor() > 280:
        bullet.hideturtle()
        bulletstate = "ready"



turtle.mainloop()
turtle.done()  
