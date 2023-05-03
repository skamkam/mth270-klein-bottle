from graphics import *

class KBAvatar:
  def __init__(self): #defines avatar and its center, initializes at the upper left corner and pointing upper left
    self.X = 115
    self.Y = 115

    self.align = "up left"
    self.body = Image(Point(self.X, self.Y), "upleft.png")


  def move_avatar(self, key, amount):
    if key == 'W': #moves up [amount] pixels
      self.body.move(0, -1*amount)
      self.Y -= amount
    elif key == 'A': #left [amount] pix
      self.body.move(-1*amount, 0)
      self.X -= amount
    elif key == 'S': #down [amount] pix
      self.body.move(0, amount)
      self.Y += amount
    elif key == 'D': #right [amount] pix
      self.body.move(amount, 0)
      self.X += amount


  def flip(self, win):
    self.body.undraw()

    center = Point(self.X, self.Y) #creates Point object at the current center so that the new image can be drawn

    if self.align == "up left":
      self.body = Image(center, 'downleft.png')
      self.align = "down left" #flips from up to down
      
    elif self.align == "down left":
      self.body = Image(center, 'upleft.png')
      self.align = "up left" #flips from down to up

    self.body.draw(win)