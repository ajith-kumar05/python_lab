#overloading


from multipledispatch import dispatch

@dispatch(str,int)
def hello(name,age):
        print("hello",name,age)

@dispatch(str)
def hello(name):
        print("hello",name)

@dispatch()
def hello():
        print("hello")

while True:
        print("Enter your choice\n1.name with age with two argument\n2.name with one argument\n3.without parameter")
        ch=int(input())
        if ch==1:
                name=input("Enter the name:")
                age=int(input("Enter the age:"))
                print("************************")
                hello(name,age)
                print("************************")
        elif ch==2:
                name=input("Enter the name:")
                print("************************")
                hello(name)
                print("************************")
        elif ch==3:
                print("Without argument")
                print("************************")
                hello()
                print("************************")
        else:
                break
