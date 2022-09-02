#fibo_time

import time
def timeit(func):
        def timed(*args,**kwrgs):
                t1=time.time()
                result=func(*args,**kwrgs)
                t2=(time.time()-t1)*10**2
                #print(min,sec)
                print("The time taken by the function is %.6f*10^-2seconds"%(t2))
                return result
        return timed

@timeit
def fib():
        a,b=0,1
        while True:
                yield a
                a,b=b,a+b
while True:
        print("*************************************************")
        ch=input("do you want enter number(y/n):")
        if (ch=="y"):
                num=int(input("Enter the number for fibonacci:"))
                fibo=fib()
                print("The fibonacci series:")

                for x in range(num):
                        print(next(fibo))
                print("*************************************************")
        elif(ch=="n"):
                print("ARIGATO,SAYONARA!")
                print("*************************************************")
                break
        else:
                print("WRONG CHOICE!!")
                print("*************************************************")
