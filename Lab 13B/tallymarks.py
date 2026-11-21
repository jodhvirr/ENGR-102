# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jodhvir Singh
# Section:      550
# Assignment:   Lab 13B
# Date:         21 November 2026

import turtle as t

screen = t.Screen()
screen.setup(800,600)


def startCursor(active_cursor, y):
    '''
    Moves the turtle to the left side of a row.

    Parameters:
        active_cursor: The turtle being moved.
        y: The vertical position of the row.
    
    '''
    
    active_cursor.penup()
    active_cursor.goto(-380, y)
    active_cursor.pendown()


def drawTally(active_cursor, digit):
    '''
    Draws tally marks based on the user's number.
    Every fifth tally is diagonal, and a new row
    begins after every 20 tally marks.

    Parameters:
        active_cursor: The turtle used for drawing.
        digit: The total number of tallies to draw.
        
    '''
    
    y = 290
    
    for i in range(1, digit+1):
        
        if i > 1 and (i - 1) % 20 == 0:
            y = moveDown(active_cursor, y)
            active_cursor.setheading(0)
        
        if i % 5 != 0:
            active_cursor.penup()
            active_cursor.forward(40)
            active_cursor.right(90)
            active_cursor.pendown()
            active_cursor.forward(75)
            active_cursor.penup()
            active_cursor.backward(75)
            active_cursor.left(90)
        
        else:
            active_cursor.forward(10)
            active_cursor.left(205)
            active_cursor.pendown()
            active_cursor.forward(170)
            active_cursor.penup()
            active_cursor.backward(170)
            active_cursor.setheading(0)
            active_cursor.forward(20)
            
            

def moveDown(active_cursor, y):
    '''
    Moves the turtle down 100 pixels to the next row
    and returns the updated Y-coordinate.

    Parameters:
        active_cursor: The turtle being moved.
        y: The current vertical position.

    Returns:
        y: The updated vertical position.
        
    '''
    
    y = y - 100
    startCursor(active_cursor, y)
    return y
    
    
    
    
def main():
    '''Asks the user for a number, creates a turtle,
    positions it, and calls the function to draw
    the tally marks.
    '''
    num = int(input("Enter a number: "))
    cursor = t.Turtle()
    startCursor(cursor, 290)
    drawTally(cursor, num)
    t.done()

main()





