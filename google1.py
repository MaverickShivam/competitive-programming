t= int(input(""))
hurrays=[]
for i in range (0,t):
    hurray=0
    n=int(input(""))
    a=input("")
    a=a.split()
    a=sorted(a, key=int)
    #print(a)
    if (len(a)==n):
        for j in range(0,n):
            for k in range (j+1,n):
                product=int(a[j])*int(a[k])
                for l in range (k+1,n):
                    if(product==int(a[l])):
                    #print(int(a[j]),"*",int(a[k]),"=",a[l])
                        hurray=hurray+1
                    else:
                        hurray=hurray+0
    else:
        hurray=("typo")
    hurrays.append(hurray)
for m in range (0,t):
    print("Case #",m+1,": ",hurrays[m])
            
    
    
    
