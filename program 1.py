#dictionary

#Creation of dictionary
Dict={}

#class creation
class Employee:
        def input(self):
                self.name=str(input("Enter the name of the employee:"))
                self.address=str(input("Enter the address of the employee:"))
                self.pan=int(input("Enter the pan number of the employee:"))
                self.basic=float(input("Enter the Basic salary of the employee:"))
                self.tds=float(input("Enter the TDS of the employee:"))
                self.hra=float(input("Enter the HRA of the employee:"))
                self.da=float(input("Enter the DA of the employee:"))
                self.deduct=float(input("Enter the deduct of the employee:"))


        def calculate(self):
                self.gross_salary=self.basic+self.hra+self.da
                self.net_amt=self.gross_salary-self.deduct

        def update(self):
                D={"Name":self.name,"Address":self.address,"Pan":self.pan,"Basic":self.basic,"TDS":self.tds,"HRA":self.hra,"DA":self.da,"Deduct":self.deduct,"Gross salary":self.gross_salary,"Net amount":self.net_amt}
                Dict.update(D)

        def search(self):
                print("Enter a key:")
                key=input()
                if key in Dict:
                        print(key,"-->",Dict[key])
                else:
                        print("no key")
while True:
        print("1.object creation")
        print("2.calculate the gross salary and net")
        print("3.update in the dictionary")
        print("4.Search the key")
        print("5.print the dictionary")
        print("6.exit the loop")
        ch=int(input("ENTER your choice:"))
        if ch==1:
                emp=Employee()
                emp.input()
        elif ch==2:
                emp.calculate()
        elif ch==3:
                emp.update()
        elif ch==4:
                emp.search()
        elif ch==5:
                print(Dict)
        else:
                break
