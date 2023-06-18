import math
class Rectangle:

    def __init__(rect, posn:tuple, w, h):
        rect.corner = posn
        rect.width = w
        rect.height = h

    def __str__(rect):
        return "({0}, {1}, {2})".format(rect.corner, rect.width, rect.height)

box = Rectangle((0, 0), 100, 200)
#bomb = Rectangle(Point(100, 80), 5, 10) # In my video game
print("box: ", box)
#print("bomb: ", bomb)

def create_rectangle (point, height, width):
   return Rectangle(point,height,width)


def str_rectangle (rect):
    return print(rect)

def shift_rectangle(rect,dx,dy):
    x= rect.corner[0]+dx
    y= rect.corner[1]+dy
    rect.corner = (x,y)


def offset_rectangle(rect,dx,dy):
    x= rect.corner[0]+dx
    y= rect.corner[1]+dy
    return Rectangle((x,y),rect.width, rect.height)

r1 = create_rectangle((10,20), 30, 40)


print (str_rectangle(r1))

shift_rectangle(r1, -10, -20)
print (str_rectangle(r1))

r2 = offset_rectangle(r1, 100, 100)
print (str_rectangle(r1)) # should be same as previous
print (str_rectangle(r2))