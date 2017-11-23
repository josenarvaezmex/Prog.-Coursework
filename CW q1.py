##This programm is calculates how fast Johnny can do a triathalaon
TotalTime=[]

def swimming():
    equipment = 1
    speed=6200.0/3600
    time =sDistance/speed*equipment
    print "Swimming""    |", "%14.2f"%(time)
    TotalTime.append(time)
    ## This function calculates the speed and time it takes for
    ## for swimming
    
def cycling():
    equipment = 1
    speed=52800.0/3600
    time=cDistance/speed*none
    print "Cycling""     |", "%14.2f"%(time)
    TotalTime.append(time)
    ## This function calculates the speed and time it takes for
    ## for cycling
    
def running():
    equipment = 1
    speed=18300.0/3600
    time=rDistance/speed*equipment
    print "running""     |",  "%14.2f"%(time)
    TotalTime.append(time)
    ## This function calculates the speed and time it takes for
    ## for running
    
while True:
    
    sDistance = float(raw_input("Please input a distance for swimming: "))
    cDistance = float(raw_input("Plese input a distance for cycling: "))
    rDistance = float(raw_input ("Please input a distance for running: "))
    ## creates a input of all the distances 
    
    if sDistance<0 or cDistance<0 or rDistance<0:
        print "Please input all postive integer numbers,"
    
    elif sDistance>=80000 or cDistance>=80000 or rDistance>=80000:
        print "Please use values below 80000 metres."
        
    else:
        
        print "Discipline  | Time Taken (s)"
        print "============|==============="
        swimming()
        cycling()
        running()

        ## This creates a table for Discipline and time taken
        
        print "For swimming distance you entered:", sDistance,"metres"
        print "For cycling distance you entered:", cDistance,"metres"
        print "For running distance you entered:", rDistance,"metres"

        print "The total time for Johnny to complete a race is:",\
        "%.2f"%(sum(TotalTime)), "Seconds."
        #this prints out all the distances travled and the speed of travel.
        
        break
