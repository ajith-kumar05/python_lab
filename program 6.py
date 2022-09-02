#student2

class student:
        def __init__(self):
                self.name=input("Enter the name:")
                self.usn=int(input("Enter the usn:"))
                self.age=int(input("Enter the age:"))
        def display(self):
                print("The name of the student:",self.name)
                print("The usn of the student:",self.usn)
                print("The age of the student:",self.age)

class derived1(student):
        def __init__(self):
                student.__init__(self)
                self.sem=input("Enter the semester:")
                self.total=0
                self.sub=[]
                for i in range(5):
                        m=int(input("Enter the marks:"))
                        self.sub.append(m)
                        self.total+=m
                self.per=self.total/5
                #derived1.display(self)
        def display(self):
                student.display(self)
                print("The semester of the the student is :",self.sem)
                print("The subject marks are:",self.sub)
                print("The total marks is:",self.total)
                print("The percentage is:",self.per)

class derived2(derived1):
        def __init__(self):
                derived1.__init__(self)
                #derived2.display(self)
        def display(self):
                derived1.display(self)

while True:
        print("Select your choice:\n1.add the details\n2.display the details")
        ch=input()
        if ch=="1":
                dr=derived2()
        elif ch=="2":
                dr.display()
        else:
                break

#student1.py


class student:
        def __init__(self):
                self.name=input("Enter the name:")
                self.usn=int(input("Enter the usn:"))
                self.age=int(input("Enter the age:"))

        def display(self):
                print("The name of the student:",self.name)
                print("The usn of the student:",self.usn)
                print("The age of the student:",self.age)

class ugstudent(student):
        def __init__(self):
                student.__init__(self)
                self.sem=input("Enter the semester:")
                self.fee=int(input("Enter the fees:"))
                self.stiphend=int(input("Enter the stiphend:"))
                ugstudent.display(self)

        def display(self):
                student.display(self)
                print("The semester of the student is:",self.sem)
                print("The fees of the student is:",self.fee)
                print("The stiphend of the student is:",self.stiphend)

class pgstudent(student):
        def __init__(self):
                student.__init__(self)
                self.sem=input("Enter the semester:")
                self.fee=int(input("Enter the fees:"))
                self.stiphend=int(input("Enter the stiphend:"))
                ugstudent.display(self)

        def display(self):
                student.display(self)
                print("The semester of the student is:",self.sem)
                print("The fees of the student is:",self.fee)
                print("The stiphend of the student is:",self.stiphend)

while True:
        print("1.ugcourse\n2.pgcourse")
        ch=input()
        if ch=="1":
                ug=ugstudent()
        elif ch=="2":
                pg=pgstudent()
        else:
                break
