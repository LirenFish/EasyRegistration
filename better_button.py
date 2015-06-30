# better_button.py
#   A simple Button widget, based on Zelle's textbook Button widget
#   but changed to be more consistent with Zelle's own graphics library!


from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(Point(30,25), 20, 10, 'Quit') """ 

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Oval(p1,p2)
        self.rect.setFill('lightgray')
        self.label = Text(center, label)
        self.activate()

    def draw(self,win):
        """Draws the button on the window"""
        self.rect.draw(win)
        self.label.draw(win)

    def undraw(self):
        """undraw the button"""
        self.rect.undraw()
        self.label.undraw()        

        
    def clicked(self, p):
        "Returns true if button active and p is inside"
        return self.active and \
               self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def setLabel(self, newText):
        "Sets the label string of this button to the specified string."
        return self.label.setText(newText)

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

    def move(self, dx, dy):
        "Move the button by offsets dx and dy"
        self.rect.move(dx, dy)
        self.label.move(dx,dy)
        
    def highlight(self,newColor):
        self.rect.setFill(newColor)
        
        

    def __str__(self):
        "returns a string/text version of this object"
        # a first stab at it, printing some useful information.
        corner1 = self.rect.getP1()
        text = "A button with top left corner at: " + str(corner1.getX()) \
               + "," + str(corner1.getY())
        text = text + " with label= " + self.label.getText()
        return text















