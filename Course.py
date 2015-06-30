## read the text file fall_2014
## Author: Liren Yu
import time
import random
from graphics import*
from timeslot_button import*
class Course:
    # constructor
    def __init__(self,code,title,time,instructor,credit,win):
        self.code=code
        self.win = win
        self.title=title
        self.time=time
        self.instructor=instructor
        self.credit=credit
        self.myTimeButtons=None
    def __str__(self):
        return self.code
    # getMethods
    def getCode(self):
        return self.code
    def getTitle(self):
        return self.title
    def getTime(self):
        return self.time
    def getInstructor(self):
        return self.instructor
    def getCredit(self):
        return self.credit
    

    def drawTime(self):
        ## splicing the time string
        daysDic = {"M":100,"T":200,"W":300,"R":400,"F":500}
        timeList = self.time.split()
        days = timeList[0] ##("MWF" "M" "TR")
        xList=[]
        for i in range(len(days)):
            xList.append(daysDic[days[i]])
        start = timeList[1]
        editedList=[]
        editedList.append(start[:start.find(":")])
        editedList.append(start[start.find(":")+1:start.find(":")+3])
        if start.find("AM") != -1:
            editedList.append("AM")
        elif start.find("PM") != -1:
            editedList.append("PM")
        else:
            editedList.append(timeList[-1])
        end = timeList[3]
        editedList.append(end[:end.find(":")])
        editedList.append(end[end.find(":")+1:end.find(":")+3])
        editedList.append(timeList[-1])
        for i in range(6):
            if i != 2 and i != 5:
                editedList[i] = float(editedList[i])
            if editedList[i] == "PM" and editedList[i - 2] != 12:
                editedList[i-2] = editedList[i-2] + 12
        startDigital =editedList[0] + editedList[1] / 60
        endDigital =editedList[3] + editedList[4] / 60
        startY = (startDigital - 8) * 50 + 50
        endY = (endDigital - 8) * 50 + 50
        ## End of splicing time string
        self.myTimeButtons = []

        colorList=["deepskyblue1","olivedrab1","violetred","coral","mediumorchid2"]
        color=colorList[random.randrange(0,5)]
        for i in range(len(xList)):
            rec = TimeSlotButton(Point(xList[i],startY),Point(xList[i]+100,endY), self.code,self)
            rec.highlight(color)
            rec.draw(self.win)
            self.myTimeButtons.append(rec)

# undrawTime is needed because when the user try to check the courses again,
# the old buttons need to be undrawn
                               
    def undrawTime(self):
        for i in range(len(self.myTimeButtons)):
            self.myTimeButtons[i].undraw()        
      
## May be useful in next version. In 2.0.1, instructor information is provided in the widget    
##    def drawInstructor(self): 
##        
##        instructor=Text(Point(800,40),self.instructor)
##        instructor.draw(self.win)

    

           


