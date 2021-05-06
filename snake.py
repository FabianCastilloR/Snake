from turtle import *
import random
from freegames import square, vector

food = vector(0, 0)        # A vector.
snake = [vector(10, 0)]    # An array of vectors.
aim = vector(0, -10)


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y
    

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = random.randrange(-15, 15) * 10
        food.y = random.randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, color1)

    square(food.x, food.y, 9, color2)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
color = ['black','green','yellow','blue','orange']    #Define the posible colors.
# Select 2 random colors from the list and check colors are not the same.
color1 = random.choice(color)
color2 = random.choice(color)
while color1 == color2:
        color1 = random.choice(color)
        color2 = random.choice(color)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()