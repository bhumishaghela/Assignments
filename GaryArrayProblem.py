""" This program takes array and queries and solves the queries"""
#taking length of array and number of queries as string
nqS=raw_input()
count=0


#counting the number of spaces in string
count=nqS.count(" ")

#checking whether space is 1
if count>1 or count<1:
    print("ERROR:Wrong input")
    exit(0)
    
#split the string to get length of array and number of queries
nqSplit=nqS.split()

#typecasting into int and getting length of array
n=int(nqSplit[0])
if n<=1 or n>=10**9:
    print("ERROR:Wrong input")
    exit(0)
    
#taking array elements as string    
aStr=raw_input()
count=aStr.count(" ")

#checking whether space is n-1
if count>=n or count<n-1:
    print("ERROR:Wrong input")
    exit(0)
aStrSplit=aStr.split()

#typecasting number of queries in int
q=int(nqSplit[1])
if q<=1 or q>=10**5:
    print("ERROR:Wrong input")
    exit(0)
qstr=[]
a=[]
#getting array elements
for i in xrange(0,n):
    if int(aStrSplit[i])<=1 or int(aStrSplit[i])>=10**5 :
        print("ERROR:Wrong input")
        exit(0)
    a.append(int(aStrSplit[i]))
    
#getting queries
for qc in xrange(0,q):
    qq=raw_input()
    # checking whether spaces are 2
    count=qq.count(" ")
    if count>=3 or count<2:
        print("ERROR:Wrong input")
        exit(0)
    qstr.append(qq)
       
#computing queries        
for qi in xrange(0,q):
    qsp=qstr[qi].split()
    q12=int(qsp[0])
    if q12==1:
        x=int(qsp[1])
        y=int(qsp[2])
        if x<0 or x>=10**5 or  y<0 or y>=10**5:
            print("ERROR:Wrong input")
            exit(0)
        a[x]=y  
    elif q12==2:
        l=int(qsp[1])
        r=int(qsp[2])
        if l<0 or l>=10**5 or  r<0 or r>=10**5:
            print("ERROR:Wrong input")
            exit(0)
        sum=0
        if  l<0 or r>len(a) or l>r or l>=len(a) or r<0 :
            print(-1)
        else:
            for i in xrange(l,r+1):
                sum=sum+a[i]
                
            print(sum)    
           
        
"""
input:
5 5
2 3 4 8 9
1 0 3
2 0 1
2 0 4
1 2 5
2 0 3
output:
6
27
19        
"""
    
    

    
