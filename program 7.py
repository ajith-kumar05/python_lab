#error


while True:
        print("1.Value error\n2.File not found error\n3.Type error\n4.Ioerror\n5.Name error")
        ch=int(input("Enter your choice:"))
        if ch==1:
                try:
                        f=open("f1.txt","z")
                        print("successful")
                except ValueError:
                        print("*******************************")
                        print("value error")
                        print("*******************************")
        elif ch==2:
                try:
                        f=open("f2.txt","r")
                        print("successful")
                except FileNotFoundError:
                        print("*******************************")
                        print("file not found error")
                        print("*******************************")
        elif ch==3:
                try:
                        f=open("f3.txt","r","w")
                        print("successful")
                except TypeError:
                        print("*******************************")
                        print("type error")
                        print("*******************************")
        elif ch==4:
                try:
                        f=open("f1","w+")
                        f.write("samplee")
                        f.close()
                        f=open("f2","r")
                        print("successful")
                except IOError:
                        print("*******************************")
                        print("Ioerror")
                        print("*******************************")
        elif ch==5:
                try:
                        f=opens("f4.txt","r")
                        print("successful")
                except NameError:
                        print("*******************************")
                        print("name error")
                        print("*******************************")
        else:
                break
