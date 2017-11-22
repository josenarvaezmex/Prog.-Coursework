TotalTime=[]

def swimming():
    none=1
    speed=(6200.0/(60*60))
    time =sDistance/speed*none
    print "Swimming""    |", "%14.2f"%(time)
    TotalTime.append(time)
    
def cycling():
    none=1
    speed=(52800.0/(60*60))
    time=cDistance/speed*none
    print "Cycling""     |", "%14.2f"%(time)
    TotalTime.append(time)
    
def running():
    none=1
    speed=(18300.0/(60*60))
    time=rDistance/speed*none
    print "running""     |",  "%14.2f"%(time)
    TotalTime.append(time)
    
while True:
    
    sDistance=float(raw_input("Please input a distance for swimming: "))
    cDistance=float(raw_input("Plese input a distnace for cycling: "))
    rDistance=float(raw_input ("Please input a distance for running: "))
    
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
        
        print "For swimming distance you entered:", sDistance,"metres"
        print "For cycling distance you entered:", cDistance,"metres"
        print "For running distance you entered:", rDistance,"metres"

        print "The total time for Johnny to complete a race is:",\
        "%.2f"%(sum(TotalTime)), "Seconds."
        
        break
