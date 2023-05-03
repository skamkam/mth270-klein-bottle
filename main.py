from graphics import *
from KBavatar import *

WIDTH = 400
HEIGHT = 400

win = GraphWin("Klein bottle", WIDTH, HEIGHT)

def square_creation(): #draws Klein bottle
  rect = Rectangle(Point(50, 50), Point(350, 350))

  leftedge = Polygon(Point(50, 200), Point(60, 210), Point(40, 210))

  rightedge = Polygon(Point(350, 210), Point(340, 200), Point(360, 200))

  topedge = Line(Point(150, 50), Point(200, 50))
  topedge.setArrow('last')

  bottomedge = Line(Point(150, 350), Point(200, 350))
  bottomedge.setArrow('last')

  kb = [rect, leftedge, rightedge, topedge, bottomedge]
  for obj in kb: #draws surface
    obj.setWidth(3)
    obj.draw(win)


def main():
  square_creation()
  avatar = KBAvatar() #creates an object of class KBAvatar
  avatar.body.draw(win) #draws the avatar to window

  win.getMouse()

  direction = ''
  while direction != 'Q':
    direction = win.checkKey().upper()
    avatar.move_avatar(direction, 5)
    
    difY = abs(avatar.Y - 200) * 2 #distance from avatar to the middle horiz line

    if avatar.X < 50: #passes left border
      avatar.flip(win) #mirror over vertical
      avatar.move_avatar('D', 300)
      if avatar.Y < 200: #above middle line
        avatar.move_avatar('S', difY)
      elif avatar.Y > 200:
        avatar.move_avatar('W', difY)

    elif avatar.X > 350: #passes right border
      avatar.flip(win)
      avatar.move_avatar('A', 300)
      if avatar.Y < 200: #above middle line
        avatar.move_avatar('S', difY)
      elif avatar.Y > 200:
        avatar.move_avatar('W', difY)

    elif avatar.Y < 50: #passes top border
      avatar.move_avatar('S', 300)

    elif avatar.Y > 350: #passes bottom border
      avatar.move_avatar('W', 300)


if __name__ == '__main__':
  main() #calls main module