import random as r

def great(n,x):
    if n>x:
        print("Too low")
    else:
        print("Too high")

def diff(n,x):
    if n>x:
        d=n-x
    else:
        d=x-n
    print(d," steps away")
    
def hcf(n,x):
    if n>x:
        d=x
    else:
        d=n
    for i in range(d,0,-1):
        if (n%i==0)and(x%i==0):
            z=i
            break;
    print("The highest common factor of the number and",x," is",z)
def lcm(n,x):
    if n<x:
        d=x
    else:
        d=n
    for i in range(d,n*x+1):
        if (i%n==0)and(i%x==0):
            z=i
            break;
    print("The least common multiple of the number and",x," is",z)


i=int(input("Choose level:\nLEVEL 1\nLEVEL 2\nLEVEL 3\nLevel no.:"))
if i==1:
    n=r.randint(1,11)
    print("The number is in the range 1 to 10")
elif i==2:
    n=r.randint(1,111)
    print("The number is in the range 1 to 100")
else:
    n=r.randint(1,1111)
    print("The number is in the range 1 to 1000")

s=100
while(s!=0):
    x=int(input("Enter the number:"))
    if x==n:
        print("CORRECT!")
        print("YOU WIN!")
        print("score:",s)
        break;
    else:
        z=r.randint(1,5)
        if z==1:
            great(n,x)
        elif z==2:
            diff(n,x)
        elif z==3:
            hcf(n,x)
        else:
            lcm(n,x)
        s=s-10
if s==0:
    print("You loose")
    print("Try again!")
