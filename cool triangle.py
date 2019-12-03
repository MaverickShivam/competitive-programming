import math
r=[]
t= int (input())
for i in range (0,t ):
    z1=0
    z2=0
    x, y = (input().split())
    x= int (x)
    y=int(y)
    xsq=x*x
    ysq=y*y
    if (x>y):
        a= math.sqrt(xsq-ysq)
        b=math.sqrt(xsq+ysq)
        val1= int (a)
        val2=int(b)
        if (val1 == a):
            z1=2         
        val2 = int(b)
        if (val2 == b):
            z2=2
    if(y>x):
        a= math.sqrt(ysq-xsq)
        b=math.sqrt(xsq+ysq)
        val1= int (a)
        val2=int(b)
        if (val1 == a):
            z1=2         
        val2 = int(b)
        if (val2 == b):
            z2=2
    if (z1+z2==0):
        r.append("False")
    else:
        r.append("True")
for k in range (0,len(r)):
    print(r[k])
        
#to check whether the given two sides of triangle are right angled or not
    #enter total trials
    #enter side lengths with a space
