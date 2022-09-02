#add_prog



import sys
import time
import math
while True:
        print("1.Display python verison\n2.display current date and time\n3.find the area of circle\n4.display name in reverse")
        ch=int(input("Enter your choice:"))
        print("********************************************************************")
        if ch==1:
                print(sys.version)
                print("********************************************************************")
        elif ch==2:
                print(time.ctime())
                print("********************************************************************")
        elif ch==3:
                r=float(input("Enter the radius: "))
                print("The area of circle with radius ",r," is : ",math.pi*r*r)
                print("********************************************************************")
        elif ch==4:
                uname=input("Enter first name :")
                lname=input("Enter last name :")
                print(lname+" "+uname)
                print("********************************************************************")
        elif ch==5:
                print("WRONG CHOICE")
                print("********************************************************************")
        else:
                print("BYE...")
                print("********************************************************************")
                break 
