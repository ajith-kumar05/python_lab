#magic

class Operator:
        def __init__(self):
                self.list1=[]

        def input(self):
                n= int(input("Enter the total length:"))
                for i in range(n):
                        ele=int(input("Enter an element:"))
                        self.list1.append(ele)

        def display(self):
                print("The list is:")
                print(self.list1)

        def __add__(self,other):
                list2=[]
                for i in range(len(self.list1)):
                        list2.append(self.list1[i]+other.list1[i])
                print("Added list is:",list2)
        def __sub__(self,other):
                list2=[]
                for i in range(len(self.list1)):
                        list2.append(self.list1[i]-other.list1[i])
                print("Subtracted list is:",list2)
        def __mul__(self,other):
                list2=[]
                for i in range(len(self.list1)):
                        list2.append(self.list1[i]*other.list1[i])
                print("multiplication of the list is:",list2)
        def __floordiv__(self,other):
                list2=[]
                for i in range(len(self.list1)):
                        list2.append(self.list1[i]//other.list1[i])
                print("Floor division of the list is:",list2)
#magic_obj


from magic import *

obj1=Operator()
obj2=Operator()

obj1.input()
obj2.input()

obj1.display()
obj2.display()

while True:
        print("""1.ADD
2.SUBTRACT
3.MULTIPLICATION
4.FLOOR DIVISION
Enter your choice:""")
        ch=int(input())
        if ch == 1:
                obj1+obj2
        elif ch==2:
                obj1-obj2
        elif ch==3:
                obj1*obj2
        elif ch==4:
                obj2//obj1
        else:
                break
