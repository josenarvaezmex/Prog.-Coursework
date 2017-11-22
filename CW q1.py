import math



def swimming():
    none=1
    speed=6200
    time =sDistance/speed*none
    print "Swimming took %.2f hours"%(time)
def cycling():
    none=1
    speed=52800
    time=cDistance/speed*none
    print "Cycling took %.2f hours"%(time)

def running():
    none=1
    speed=18300
    time=rDistance/speed*none
    print "Running took %.2f hours"%(time)


sDistance=int(raw_input("Please input a distance for swimming: "))
cDistance=int(raw_input("Plese input a distnace for cylcing: "))
rDistance=int(raw_input ("Please input a distance for running: "))

while True:

    if sDistance<0 or cDistance<0 or rDistance<0:
        print "Please input all postive integer numbers"
        sDistance=int(raw_input("Please input a distance for swimming: "))
        cDistance=int(raw_input("Plese input a distnace for cylcing: "))
        rDistance=int(raw_input ("Please input a distance for running: "))

    else:
        print "For swimming distance you entered:", sDistance,"metres"
        print "For cycling distance you entered:", cDistance,"metres"
        print "For running distance you entered:", rDistance,"metres"
        swimming()
        cycling()
        running()
        break
