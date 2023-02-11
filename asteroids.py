import turtle
import mosaic
import turtle_interpreter2
import random

class Game:
    def __init__(self):  
        '''This is the constructor of the game where the baclground is created, the player is defined
        the enemies are defined, the setUpEvents is called, the top third is defined, the collisons distance
        is defined'''
        self.terp = turtle_interpreter2.TurtleInterpreter()
        self.screen = self.terp.getScreen()
        mosaic.mosaic(-2, -2, 200, 4, 4)
        self.player = self.makePlayer()
        self.distance = 20
        self.setupEvents()
        self.xMax = 400
        self.yMax = 400
        self.xMin = -400
        self.yMin = 133
        self.enemies = self.makeEnemies(10)
        self.collision = 30
        
    def play(self):
        '''Turns the tracer animations on (but speeds up animations) and starts the main game loop.
        '''
        # Call the tracer method on your `Screen` instance variable,
        # passing in True as the parameter to turn animations on.
        self.screen.tracer(True)
        # Call the listen method on your `Screen` instance variable
        # so that keyboard presses are not registered as events
        self.screen.listen()
        # Call the mainloop method on your `Screen` instance variable
        self.screen.mainloop()

    def makePlayer(self):
        '''This function creates the player turtle object which is a rocket ship. Credit
        to the original author https://blog.trinket.io/using-images-in-turtle-programs/ Brian Marks'''
        self.player = turtle.Turtle()
        self.screen.register_shape('rocketship.gif')
        self.player.shape('rocketship.gif')
        self.player.penup()
        self.player.setheading(90)
        return self.player

    def setupEvents(self):
        '''This function lets the player move up down left right and turn. It also sets the
        timer for the enemies to move randomly and the check collisions timer'''
        self.screen.onkeypress(self.moveUp, "Up")
        self.screen.onkeypress(self.moveDown, "Down")
        self.screen.onkeypress(self.moveRight, "Right")
        self.screen.onkeypress(self.moveLeft, "Left")
        self.screen.onkeypress(turtle.bye, "q")

        self.screen.ontimer(self.moveEnemiesRandomly, 50)
        self.screen.ontimer(self.checkCollisions, 50)

    def moveUp(self):
        '''move rocket up by self.distance'''
        #self.player.setheading(90)
        self.player.forward(self.distance)

    def moveDown(self):
        '''move rocket down by self.distance'''
        #self.player.setheading(270)
        self.player.backward(self.distance)

    def moveRight(self):
        '''move rocket right by self.distance'''
        #self.player.setheading(0)
        self.player.right(self.distance)

    def moveLeft(self):
        '''move rocket left by self.distance'''
        #self.player.setheading(180)
        self.player.left(self.distance)

    def placeEnemyRandomly(self, turt):
        '''This function randomly places the enemies in the top third of the screen'''
        turt.goto((random.randint(-400, 400)), (random.randint(133, 400)))


    def makeEnemies(self, n):
        '''This function makes a list of n enemies, makes them squares, colors them black, and 
        calls the place enemy randomly function so they are put in random positions'''
        my_enemies = []
        for i in range (n):
            my_enemies.append(turtle.Turtle())
        for i in my_enemies:
            i.shape('square')
            i.color('black')
            i.penup()
            self.placeEnemyRandomly(i)
        return my_enemies

    def moveEnemiesRandomly(self):
        '''This function lets the enemies move arounf the screen in random directs every 50 mseconds'''
        for i in self.enemies:
            newX = i.xcor() + random.randint(-5, 5)
            newY = i.ycor() + random.randint(-5, 5)
            i.goto(newX, newY)
        self.screen.ontimer(self.moveEnemiesRandomly, 50)


    def checkCollisions(self):
        '''This function checks to see if the player has gotten within 30 pixels of the enemy. If
        it has the enemy disapears and BOOM is written in the terminal'''
        for i in self.enemies:
            enemy_x = i.xcor()
            enemy_y = i.ycor()

            if abs(self.player.xcor() - enemy_x) < self.collision and abs (self.player.ycor() - enemy_y) < self.collision:
                i.hideturtle()
                print("BOOM")
                self.placeEnemyRandomly(i)

        self.screen.ontimer(self.checkCollisions, 50)
        

if __name__ == '__main__':
    game = Game()
    game.play()
