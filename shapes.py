'''
Hannah Soria
Professor Wolfe
CS151 fall 2021
Project 9 Shapes and Mosaics
'''

import turtle_interpreter2

class Shape:
    def __init__(self, distance=100, angle=90, color=(0, 0, 0), lsysString=''):
        
        '''Shape constructor

        Parameters:
        -----------
        distance: float. Distance in pixels to go when moving the turtle forward
        angle: float. Angle in degrees to turn when turning the turtle left/right
        color: tuple of 3 floats. Default turtle pen color
        lsysString: str. The L-system string of drawing commands to draw the shape
            (e.g. made up of 'F', '+', '-', ...)
        '''
        # Create an instance variable for a new TurtleInterpreter object
        self.ti = turtle_interpreter2.TurtleInterpreter()
        # Create instance variables for all the parameters
        self.distance = distance
        self.angle = angle
        self.color = color
        self.lsysString = lsysString
        
        

    def getTI(self):
        return self.ti

    def getString(self):
        return self.lsysString

    def setColor(self, c):
        self.color = c 

    def setDistance(self, dist):
        self.distance = dist

    def setAngle(self, a):
        self.angle = a

    def setString(self, s):
        self.lsysString = s

    def draw(self, x_pos, y_pos, scale=1.0, heading=0):
        '''Draws the L-system string at the position `(x, y)` = `(x_pos, y_pos)` with the turtle
        facing the heading `heading`. The turtle drawing distance is scaled by `scale`.
        '''
        self.ti.setColor(self.color)
        self.ti.goto(x_pos, y_pos, heading)
        self.ti.drawString( self.lsysString, self.distance * scale, self.angle)
        
        
class Square(Shape):
    '''In this class a square is drawn and it takes in distance, color and a fill.'''
    def __init__(self, distance=100, color=(0, 0, 0), fill=False):
  # Create a variable for the L-system string that would draw a square.
        square = 'F+F+F+F'
        lsysString = square
        #self.ti.setColor(color)
  # if the fill parameter is true, concatenate the { and } characters
  # to the beginning and end of the L-system string,
  # updating the value of the L-system string.
        if fill == True:
            lsysString = '{' + square + '}'
  # Call the parent's constructor, passing along values for all its
  # parameters.
        Shape.__init__(self, distance, 90, color, lsysString)

class Hexagon(Shape):
    '''In this class a hexagon is drawn and it takes in distance, color and a fill. This class inherits from the Shape class.'''
    def __init__(self, distance=100, color=(0, 0, 0), fill=False):
        hexagon = 'F+F+F+F+F+F'
        lsysString = hexagon
        if fill == True:
            lsysString = '{' + hexagon + '}'
        Shape.__init__(self, distance, 60, color, lsysString)
    
class Rectangle(Shape):
    '''In this class a rectangle is drawn and it takes in distance, color and a fill. This class inherits from the Shape class.'''
    def __init__(self, distance= 100, color=(0, 0, 0), fill=False):
        rectangle = 'F+FF+F+FF'
        lsysString = rectangle
        if fill == True:
            lsysString = '{' + rectangle + '}'
        Shape.__init__(self, distance, 90, color, lsysString)

class Triangle(Shape):
    '''In this class a triangle is drawn and it takes in distance, color and a fill. This class inherits from the Shape class.'''
    def __init__(self, distance= 100, color=(0, 0, 0), fill=False):
        triangle = 'F+F+F'
        lsysString = triangle
        if fill == True:
            lsysString = '{' + triangle + '}'
        Shape.__init__(self, distance, 120, color, lsysString)

class Star(Shape):
    '''In this class a star is drawn and it takes in distance, color and a fill. This class inherits from the Shape class.'''
    def __init__(self, distance=100, color=(0, 0, 0), fill=False):
        star = 'F+F+F+F'
        lsysString = star
        if fill == True:
            lsysString = '{' + star + '}'
        Shape.__init__(self, distance, 145, color, lsysString)


def test():
    '''In this funtion each of the shape classes is created and called to draw'''
    testrectangle = Rectangle(color = 'yellow', fill = True)
    testrectangle.draw(-200,0)
    testtriangle = Triangle(color = 'purple', fill = False)
    testtriangle.draw(-250,-250)
    testhexagon = Hexagon(color = 'red', fill = True)
    testhexagon.draw(0,0)
    testsquare = Square(color = 'green', fill = False)
    testsquare.draw(250,250)
    teststar = Star(color = 'pink', fill = True)
    teststar.draw(0, -100)
    testsquare.getTI().hold()


if __name__ == '__main__':
    test()