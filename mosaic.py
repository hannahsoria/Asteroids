'''
Hannah Soria
Professor Wolfe
CS151 fall 2021
Project 9 Shapes and Mosaics
'''

import shapes

def tile(x, y, scale, hold = False):
    '''This function creates a tile made up of squares, hexagons, stars, rectangles, and triangles from the Shapes class
    All of the shapes are drawn on top of the square and to scale so that the entire tile moves and scales as one unit.'''
    square1 = shapes.Square(distance = 1 * scale, color = 'DarkBlue', fill = True)
    square1.draw(x * scale, y * scale)
    hexagon1 = shapes.Hexagon(distance = .1 * scale, color = 'lightblue', fill = True)
    hexagon1.draw((x + .1) * scale, (y + .1 )* scale)
    star1 = shapes.Star(distance = .1 * scale, color = 'DarkGoldenrod1', fill = True)
    star1.draw((x + .1) * scale, (y + .175) * scale)
    hexagon2 = shapes.Hexagon(distance = .1 * scale, color = 'lightblue', fill = True)
    hexagon2.draw((x + .8) * scale, (y + .1 )* scale)
    star2 = shapes.Star(distance = .1 * scale, color = 'DarkGoldenrod1', fill = True)
    star2.draw((x + .8) * scale, (y + .175) * scale)
    hexagon3 = shapes.Hexagon(distance = .1 * scale, color = 'lightblue', fill = True)
    hexagon3.draw((x + .45) * scale, (y + .1 )* scale)
    star3 = shapes.Star(distance = .1 * scale, color = 'DarkGoldenrod1', fill = True)
    star3.draw((x + .45) * scale, (y + .175) * scale)
    hexagon4 = shapes.Hexagon(distance = .1 * scale, color = 'lightblue', fill = True)
    hexagon4.draw((x + .45) * scale, (y + .7 )* scale)
    star4 = shapes.Star(distance = .1 * scale, color = 'DarkGoldenrod1', fill = True)
    star4.draw((x + .45) * scale, (y + .78) * scale)
    hexagon5 = shapes.Hexagon(distance = .1 * scale, color = 'lightblue', fill = True)
    hexagon5.draw((x + .1) * scale, (y + .7 )* scale)
    star5 = shapes.Star(distance = .1 * scale, color = 'DarkGoldenrod1', fill = True)
    star5.draw((x + .1) * scale, (y + .78) * scale)
    hexagon6 = shapes.Hexagon(distance = .1 * scale, color = 'lightblue', fill = True)
    hexagon6.draw((x + .8) * scale, (y + .7 )* scale)
    star6 = shapes.Star(distance = .1 * scale, color = 'DarkGoldenrod1', fill = True)
    star6.draw((x + .8) * scale, (y + .78) * scale)
    rectangle1 = shapes.Rectangle(distance = .1 *scale, color = 'DarkSlateGray1', fill = False)
    rectangle1.draw((x + .1) * scale, (y + .4 )* scale)
    rectangle2 = shapes.Rectangle(distance = .1 *scale, color = 'DarkSlateGray1', fill = False)
    rectangle2.draw((x + .8) * scale, (y + .4 )* scale)
    triangle1 = shapes.Triangle(distance = .3 * scale, color = 'white', fill = True)
    triangle1.draw((x + .35) * scale, (y + .35 )* scale)
    triangle2 = shapes.Triangle(distance = .1 * scale, color = 'DarkBlue', fill = True)
    triangle2.draw((x + .45) * scale, (y + .4 )* scale)
    #if hold == True:
    #    triangle2.getTI().hold()


def mosaic(x, y, scale, Nx, Ny):
    '''This function draws a mosaic which is a grid tiles made up from the tile created in the function above. 
    The function created a grid which the specifications are given in the parameters. The specifications determine
    how many tiles are drawn.'''
    x_init = x
    for row in range (Ny):
        for col in range(Nx):
            #if row == Ny - 1 and col == Nx - 1:
            #    hold = True
            #else:
            #    hold = False
            x = x_init + col
            tile(x, y, scale, hold = False)
        x = x_init
        y = y + 1



if __name__ == '__main__':
    mosaic(-2, -2, 200, 4, 4)
    #tile(0,0,100,True)
    
    