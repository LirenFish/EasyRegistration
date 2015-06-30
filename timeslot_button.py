# TimeSlotButton!!!
# An advanced version of better_button
# Author: Liren Yu


from graphics import *

class TimeSlotButton:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, Point1, Point2,code,course):
        """ Creates a rectangular button, eg:
        qb = Button(Point(30,25), 20, 10, 'Quit') """ 
        self.Point1=Point1
        self.Point2=Point2
        self.rect = Rectangle(Point1,Point2)
        self.code=code
        self.txt = Text(self.rect.getCenter(), self.code)
        self.course = course
        self.activate()
    def getPoint1(self):
        return self.Point1
    def getPoint2(self):
        return self.Point2
    def getRect(self):
        return self.rect
    def getCourse(self):
        return self.course
    
    def draw(self,win):
        """Draws the button on the window"""
        self.rect.draw(win)
        self.txt.draw(win)

    def undraw(self):
        """undraw the button"""
        self.rect.undraw()
        self.txt.undraw()
    
        
    def clicked(self, p):
        "Returns true if button active and p is inside"
        return self.getPoint1().getX()< p.getX()and p.getX() < self.getPoint2().getX() and self.getPoint1().getY()< p.getY()and p.getY() < self.getPoint2().getY()
        
##        return self.active and \
##               self.Point1.getX()<= p.getX() <= self.Point1.getX() and \
##               self.Point1.getY() <= p.getY() <= self.Point2.getY()
##


    def activate(self):
        "Sets this button to 'active'."
        
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        
        self.rect.setWidth(1)
        self.active = False

    def move(self, dx, dy):
        "Move the button by offsets dx and dy"
        self.rect.move(dx, dy)
        
    def highlight(self,newColor):
        self.rect.setFill(newColor)
        self.rect.setOutline(newColor)

    def setOutline(self,color):
        self.rect.setOutline(color)

    def __str__(self):
        "returns a string/text version of this object"
        
        corner1 = self.rect.getP1()
        text = "A button with top left corner at: " + str(corner1.getX()) \
               + "," + str(corner1.getY())
        text = text + " with Course: " + str(self.getCourse())
        return text















