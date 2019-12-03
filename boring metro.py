#input values with space

for i in range(0, 1):
    l1=[]
    p=0
    k=(input().split())
    for i in range (1,len(k)):
        k[i-1]=int(k[i-1])
        k[i]=int(k[i])
        a=k[i]-k[i-1]
        l1.append(a)
    if (l1[0]<0):
        l1.insert(0,1)
    z=len(l1)
    if(l1[z-1]>0): 
        l1.append(-1)
    m=len(l1)
    for i in range(0,z-2):
        if (l1[i]>0):
            if (l1[i+1]>0):
                p=p+1
        if (l1[i]<0):
            if (l1[i+1]<0):
                p=p+1
    s=int(((m-p)/2)+1)
print(s)
a= input()

        
                      
 
