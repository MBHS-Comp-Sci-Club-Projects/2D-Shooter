import turtle


def inside_window(x, y):
    # Changed condition to use absolute values and a more reasonable window boundary
    if abs(x) > 500 or abs(y) > 500:
        return False
    else:
        return True


class Bullet(turtle.Turtle):

    def __init__(self, color: str, x, y, direction: str):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.shape("arrow")
        self.color(color)
        self.speed(0)
        self.direction = direction # Save the direction

        if direction == "up":
            self.setheading(90)
        elif direction == "down":
            self.setheading(270)
        elif direction == "left":
            self.setheading(180)
        elif direction == "right":
            self.setheading(0)

    def move(self):
        # Moved bullet movement to a separate method
        self.forward(10)

    def get_x(self):
        return self.xcor()

    def get_y(self):
        return self.ycor()

    def is_inside_window(self):
        return inside_window(self.xcor(), self.ycor())


class Person(turtle.Turtle):

    def __init__(self, color: str, x, y):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color(color)
        self.speed(0)
        self.playerColor = color
        self.bullets = []
        self.setpos(x, y)
        self.lives = 3

    def get_x(self):
        return self.xcor()

    def get_y(self):
        return self.ycor()

    def move_up(self):
        self.setheading(90)
        self.forward(20) # increased movement speed

    def move_down(self):
        self.setheading(270)
        self.forward(20) # increased movement speed

    def move_left(self):
        self.setheading(180)
        self.forward(20) # increased movement speed

    def move_right(self):
        self.setheading(0)
        self.forward(20) # increased movement speed

    def is_touching(self, x, y):
        # Modified collision detection to use distance formula
        distance = ((self.xcor() - x) ** 2 + (self.ycor() - y) ** 2) ** 0.5
        if distance < 20: # reduced collision detection distance
            return True
        else:
            return False

    def launch_bullet(self):
        x, y = self.pos()
        # Bullet now gets its heading from the player.
        bullet = Bullet(self.playerColor, x, y, self.heading())
        self.bullets.append(bullet)


def update():
    if player1.is_touching(player2.get_x(), player2.get_y()):
        player1.lives -= 1
        player2.lives -= 1
        player1.goto(-180,100) #send players back to start
        player2.goto(180,0) #send players back to start

    if player1.lives <= 0:
        print("Player 2 wins!")
        turtle.bye() # close the window
    elif player2.lives <= 0:
        print("Player 1 wins!")
        turtle.bye() # close the window

    bullets_to_remove_p1 = []
    for bullet in player1.bullets:
        bullet.move()
        if not bullet.is_inside_window():
            bullets_to_remove_p1.append(bullet)
        elif player2.is_touching(bullet.get_x(), bullet.get_y()):
            bullets_to_remove_p1.append(bullet)
            player2.lives -= 1

    for bullet in bullets_to_remove_p1:
        player1.bullets.remove(bullet)
        bullet.hideturtle() #remove bullet from screen

    bullets_to_remove_p2 = []
    for bullet in player2.bullets:
        bullet.move()
        if not bullet.is_inside_window():
            bullets_to_remove_p2.append(bullet)
        elif player1.is_touching(bullet.get_x(), bullet.get_y()):
            bullets_to_remove_p2.append(bullet)
            player1.lives -= 1

    for bullet in bullets_to_remove_p2:
        player2.bullets.remove(bullet)
        bullet.hideturtle() #remove bullet from screen

    window.ontimer(update, 30) # Animation loop


def create_window(windowWidth: int, windowHeight: int, bgcolor: str):
    window = turtle.Screen()
    window.setup(windowWidth, windowHeight)
    window.bgcolor(bgcolor)
    return window


player1 = Person("red", -180, 100)
player2 = Person("blue", 180, 0)

window = create_window(1000, 1000, "white")

window.listen()
window.onkeypress(player1.move_up, "w")
window.onkeypress(player1.move_down, "s")
window.onkeypress(player1.move_left, "a")
window.onkeypress(player1.move_right, "d")
window.onkeypress(player1.launch_bullet, "Return")

window.onkeypress(player2.move_up, "Up")
window.onkeypress(player2.move_down, "Down")
window.onkeypress(player2.move_left, "Left")
window.onkeypress(player2.move_right, "Right")
window.onkeypress(player2.launch_bullet, "space")

update() # Start the animation loop
window.mainloop() #better version