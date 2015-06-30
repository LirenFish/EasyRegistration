## Author: Liren Yu   Email: liren.yu@centre.edu
## Course: CSC 117 Fall 2013
## Final Project: Easy Registration
##
## Assistance:
##     - I wrote this code with no assistance other than that listed here
##         I got some help from Ye Sheng on how to splice those non-regular
##         strings from the course information txt file.
##     - I provided assistance to the following:
##         I helped Shaoyu Yuan on how to create a Class.
##
## Self Assessment & Caveats:
##     - I think this project meets the requirement, because it is super nifty.
##      Easy Registration is not just something I did for CSC 117 final project,
##       it is actually useful. Before the Centrenet registration page provides a virtual
##      schedule viewer, this program is a powerful substitution. It makes life
##      easier, although there is no Dragons, Ninjas or fireballs.
##      Plus, I use three Classes in this program.
##     
##
## Wish List:
##     - Make the window look better!
##     - try to make the professor name linking to his or her introduction page
##       on archive.centre.edu
##     - find the text book informaion
##
## Time:
##     - 22 Hour working on it
##     - I am thinking about it unless I am not awake.
## Reflection:
##     - A good stucture is important.
##     - Make the code more generlized. Otherwise, when adding new features,
##       the original code has to be rewritten.
##     - A Class is useful. Because it stores information. If one uses a function,
##      he has to pass in and pass out variables. Class can save one a lot of work.
##      Also, the attibutes are like small functions. When ever a new function is
##      needed, just add another attibute to the Class, which is handy.


from graphics import*
from better_button import*
from Course import*

def setUpWindow():
    win=GraphWin("Easy Registration 2.0.1",850,455)  # set the window
    win.setBackground("white")
    # set up buttons
    check=Button(Point(640,245),55,40,'Check')
    check.draw(win)    
    submit=Button(Point(725,245),55,40,'Submit')  
    submit.draw(win)
    Exit=Button(Point(810,245),55,40,'Exit')
    Exit.draw(win)    

    #set up all the entry boxes for 6 courses
    courseEntries=[]
    for i in range(0,6,1):
        courseEntry=Entry(Point(700,40+30*i),9)
        courseEntry.draw(win)
        courseEntries.append(courseEntry)

    # number the courses
    for i in range(0,6,1):
        courselabels=Text(Point(650,40+30*i),str(i+1))
        courselabels.draw(win)

    #set up the area of the time table
    timeTableArea=Rectangle(Point(3,3),Point(605,453))# i don't know why i substract 5
    timeTableArea.setWidth(4)
    timeTableArea.draw(win)

    #set up the area of course information widget
    informationWidget=Rectangle(Point(615,273),Point(845,450))
    informationWidget.setWidth(2)
    informationWidget.draw(win)
    informationWidget=Rectangle(Point(618,276),Point(840,445))
    #informationWidget.setWidth(0.5)
    informationWidget.draw(win)
    
    
##  # Draw the Grids
##  commented out because it may look better without grids.
##    for i in range (0,450,50):
##       horizontalLine=Line(Point(0,i),Point(600,i))
##       horizontalLine.draw(win)
##    for i in range(0,600,100):
##        verticalLine=Line(Point(i,0),Point(i,450))
##        verticalLine.draw(win)


    #label the day
    weekDayList=["Monday","Tuesday","Wednesday","Thursday","Friday"]
    ii=0
    for i in range(150,600,100):
        weekDayLabel=Text(Point(i,25),weekDayList[ii])
        weekDayLabel.draw(win)
        ii+=1
    
    #label the time
    timeList=["8:00","9:10","10:20","11:30","12:40","13:50","15:00"]
    for i in range(len(timeList)):
        H_M_List=timeList[i].split(":")
        Hour=float(H_M_List[0])+float(H_M_List[1])/60
        timeLabel=Text(Point(50,50*(Hour-8.0)+50),timeList[i])
        timeLabel.draw(win)
    return [win, courseEntries,submit,check,Exit] #what should i return

# Get the Course Code
def getCourseFromEntryBox(entryBox):# the captitalization of course code 
    courseInput=entryBox.getText()
    courseList=courseInput.split()
    try:
        courseInput=courseList[0].upper()+" "+ courseList[1]
        return courseInput
    except:
        return courseInput

# Search through the fall_2014 file to find out information about that course
def findCourseInformation(course1,win):
    fin=open('fall_2015.txt','r')
    wholeText=fin.readlines()
    # wholeText is a list of 2734 strings. Each string is a line in the txt file
    for i in range(len(wholeText)):
        if course1 in wholeText[i]: # check if the input course name is in Fall_2014
            endTitle=wholeText[i].find("required")-1
            startTitle=11 # after 11 characters
            course1_title=wholeText[i][startTitle:endTitle]
            course1_instructor=wholeText[i+1][0:-1]
            endTime=wholeText[i+3].find(";")
            course1_time=wholeText[i+3][:endTime] # read three more lines 
            course1_credit=wholeText[i+4][:3]
            # HERE the COURSE OBJECT IS CREATED
            courseClass=Course(course1,course1_title,course1_time,course1_instructor,course1_credit,win)
            return courseClass
            
    return None #"Course DNE"


def findAllButtons(courseList):
    timeSlotButtonList=[] # initial the list
    for i in range(len(courseList)):
        for ii in range(len(courseList[i].myTimeButtons)):# loop through all the buttons
            timeSlotButtonList.append(courseList[i].myTimeButtons[ii])
    return timeSlotButtonList
## THIS is an alternative way to loop through all the buttons. 
## It is shorter than the above one, but indexs make the code clear.
##    for course in courseList:
##        for button in course.myTimeButtons:
##            timeSlotButtonList.append(button)  



def isOverlapBetweenTwoRects(rect1,rect2):
    diffColumns=not bool(rect1.getP1().getX()== rect2.getP1().getX())
    rect1Above= rect1.getP2().getY()<=rect2.getP1().getY() 
    rect2Above=rect2.getP2().getY()<=rect1.getP1().getY()
    return not (diffColumns or rect1Above or rect2Above)
## This is an alternative way to check if two rectangles overlap each other.
## Although it works but it is way more complicated than the above one.
## It checks the condition of overlapping but the above one checks the negation
## of overlapping. Sometimes checking the negation condition is useful!!!
##def isTwoRecOverlap(rect1,rect2):
##    return not isNotOverlap(rect1,rect2)
##    sameColumn=bool(rect1.getP1().getX()== rect2.getP1().getX())
##    B=bool(rect1.getP1().getY()<rect2.getP2().getY())and bool(rect1.getP2().getY()>rect2.getP1().getY())
##    C=bool(rect2.getP1().getY()<rect1.getP2().getY())and bool(rect2.getP2().getY()>rect1.getP1().getY())
##    
##    return sameColumn and (B or C)

def checkConflicts(List):
# compare each pair in the list
# For example the first element is compared to all the elements after it.
# from the second to the end. The second element is compared to those from
# the third to the end, etc. Therefore, save half of the comparsion work.

    for i in range(len(List)-1):
        for ii in range(i+1,len(List)):
            if isOverlapBetweenTwoRects(List[i].getRect(),List[ii].getRect()):
                List[i].highlight('')
                List[ii].highlight('')
                List[i].setOutline("RED")
                List[ii].setOutline("RED")
    


def main():
    returnOfSetUpWindow=setUpWindow()
    win=returnOfSetUpWindow[0] # the window
    courseEntries=returnOfSetUpWindow[1]# the courseEntries List
    submit=returnOfSetUpWindow[2]
    check=returnOfSetUpWindow[3]
    Exit=returnOfSetUpWindow[4]
    Confirm_course=Text(Point(800,40+30)," ")#set up the initial value for Course Feedback
    Error_courseDNE=Text(Point(800,40+30)," ")
    Confirm_course.draw(win)
    Error_courseDNE.draw(win)
    feedback=[]
    courseList=[]
    # initiate the loop of checking courses
    clickedPoint=Point(0,0)
    while not(check.clicked(clickedPoint)): #getMouse()until the botton is clicked
            clickedPoint=win.getMouse()        

    # the loop of checking courses, stop when Submit
    while not (submit.clicked(clickedPoint)):
        for i in range(len(feedback)):# undraw the feedback, the course information
            feedback[i].undraw()
        for i in range(len(courseList)):
            courseList[i].undrawTime()
        courseList=[] 
        feedback=[]
        timeSlotButtonList=[]
        for i in range(6):
            courseCode=getCourseFromEntryBox(courseEntries[i])
            if courseCode != "":
                theCourse=findCourseInformation(courseCode,win)
                if theCourse!= None:# if the course can be found in Fall_2014
                    courseList.append(theCourse)
                    theCourse.drawTime()
                    Confirm_course=Text(Point(800,40+30*i),":  )")
                    Confirm_course.draw(win)
                    feedback.append(Confirm_course)
                else:# if the course cannot be found, i.e. it is not offered
                    Error_courseDNE=Text(Point(800,40+30*i),": ( Not Offered")
                    Error_courseDNE.draw(win)
                    feedback.append(Error_courseDNE)

        # Find all the buttons and check if course schedule has a conflict issue
        timeSlotButtonList=findAllButtons(courseList)
        checkConflicts(timeSlotButtonList) 
        # getMouse to set a new clickedPoint value
        clickedPoint=win.getMouse()
        # End of the Checking loop by clickin the Submit button.
        


## This is a new stage of this program. The user has submitted all the courses;
## thus, the schedule is fixed. In turn, he can click on the courses buttons, and
## check the detailed course information
    title=Text(Point(720,320),"") #set the initial value of all the Text object
    code=Text(Point(720,300),"")
    instructor=Text(Point(700,360),"")
    credit=Text(Point(700,400),"")

    while not(Exit.clicked(clickedPoint)):
    ## loop unitl the Exit button is clicked    
        title.undraw()
        code.undraw()
        instructor.undraw()
        credit.undraw()
        for aBotton in timeSlotButtonList: # Check if the click in any one of the buttons
            if aBotton.clicked(clickedPoint):# if is, the course information would be drawn
                title=Text(Point(730,320),aBotton.getCourse().getTitle())
                code=Text(Point(730,300),aBotton.getCourse().getCode())
                instructor=Text(Point(730,360),"    Professor: "+aBotton.getCourse().getInstructor())
                credit=Text(Point(730,400),"Credit Hours:  "+aBotton.getCourse().getCredit())
                
                code.draw(win)
                title.draw(win)
                instructor.draw(win)
                credit.draw(win)
        clickedPoint=win.getMouse()      
    
    win.close() 


if __name__ == "__main__":
    main()
