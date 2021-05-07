# Código modificado por:
# Autor: Fabián Castillo Rodríguez
# Autor: Sergio Adolfo Sanoja Hernández

from turtle import *
import random
from freegames import square, vector


food = vector(0, 0)        # The initial food's position.
snake = [vector(10, 0)]    # The initial snake's position.
aim = vector(0, -10)       # The initial snake's direction.
foodmov = vector(0,-10)    # The initial food's direction.


def change(x, y):
    """
    Change direction of the snake.
    """
    # Update x & y values.
    aim.x = x
    aim.y = y


def inside(head):
    """
    Return True if head inside boundaries.
    """
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """
    Move snake forward one segment.
    """
    head = snake[-1].copy()    # Set head as the las unit of snake.
    head.move(aim)             # Make the snake move in aim's direction.

    # Assign a random food's movement direction.
    movx = random.randrange(-10,11,10)
    movy = random.randrange(-10,11,10)

    # Make sure that the food doesn't return to the last position.
    while movx == -foodmov.x and movy == -foodmov.y:
        movx = random.randrange(-10,11,10)
        movy = random.randrange(-10,11,10)

    # Assure that the food stays within the boundries.
    if food.x > 180:
        movx = -10
    if food.x < -190:
        movx = 10
    if food.y > 180:
        movy = -10
    if food.y < -190:
        movy = 10

    # Updates food's movement direction.
    foodmov.x = movx
    foodmov.y = movy

    food.move(foodmov)    # Make the food move in foodmov's direction.

    # Stop the game when the snake touches the boundries.
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)    # Add a unit to the snake.

    # When the head is in the same place as the food, it is located in
    # a new random position.
    if head == food:
        print('Snake:', len(snake))
        food.x = random.randrange(-15, 15) * 10
        food.y = random.randrange(-15, 15) * 10
    else:
        snake.pop(0)    # Delete a unit from the snake.

    clear()

    # Generate the shape of the snake's and food's units.
    for body in snake:
        square(body.x, body.y, 9, color1)
    square(food.x, food.y, 9, color2)

    update()
    ontimer(move, 100)    # Set the movement rate.

setup(420, 420, 370, 0)    # Create the workspace.
color = ['black','green','yellow','blue','orange']    #Define the posible colors.

# Select 2 random colors from the list and check colors are not the same.
color1 = random.choice(color)
color2 = random.choice(color)
while color1 == color2:
        color1 = random.choice(color)
        color2 = random.choice(color)

hideturtle()
tracer(False)              # Deactivate the turtle's animation.
listen()                   # Prepare the turtle to receive directions.

# Define the keys to change direction.
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()    # Call the function.
done()
