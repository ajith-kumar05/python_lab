#overriding

class employee:
        raise_amt=1.04
        def __init__(self):
                self.first=input("Enter the first name:")
                self.last=input("Enter the last name:")
                self.empid=input("Enter the employee id:")
                self.pay=int(input("Enter the pay:"))

        def apply_raise(self):
                self.pay=self.pay*self.raise_amt
                employee.display(self)

        def display(self):
                print("The first name of the Employee:",self.first)
                print("The last name of the Employee:",self.last)
                print("The employee id:",self.empid)
                print("The pay amount:",self.pay)

class developer(employee):
        raise_amt=2.05
        def __init__(self):
                super().__init__()

        def apply_raise(self):
                self.pay=self.pay*self.raise_amt
                super().display()

class manager(employee):
        raise_amt=3.05
        def __init__(self):
                super().__init__()

        def apply_raise(self):
                self.pay=self.pay*self.raise_amt
                super().display()

while True:
        print("Enter your choice:\n1.Enter the employee details:\n2.Enter the developer details:\n3.Enter the manager details:")
        print("4.To apply raise on employee:\n5.To apply raise on developer:\n6.To apply raise on manager:")
        print("7.To display employee details:\n8.To display developer details:\n9.to display manager details:")
        ch=int(input())
        if 1==ch:
                print("******************************************************")
                emp1=employee()
                print("******************************************************")
        elif 2==ch:
                print("******************************************************")
                emp2=developer()
                print("******************************************************")
        elif 3==ch:
                print("******************************************************")
                emp3=manager()
                print("******************************************************")
        elif 4==ch:
                print("******************************************************")
                print("applied raise:",emp1.raise_amt)
                emp1.apply_raise()
                print("******************************************************")
        elif 5==ch:
                print("******************************************************")
                print("applied raise:",emp2.raise_amt)
                emp2.apply_raise()
                print("******************************************************")
        elif 6==ch:
                print("******************************************************")
                print("applied raise:",emp3.raise_amt)
                emp3.apply_raise()
                print("******************************************************")
        elif 7==ch:
                print("******************************************************")
                emp1.display()
                print("******************************************************")
        elif 8==ch:
                print("******************************************************")
                emp2.display()
                print("******************************************************")
        elif 9==ch:
                print("******************************************************")
                emp3.display()
                print("******************************************************")
        else:
                break
