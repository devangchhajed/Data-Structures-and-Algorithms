import math
arr1=[]
arr2=[]
arr3=[]
xlist=[]

def onedlist(a):
    if isinstance(a[0], list)==True:
        for i in a:
            onedlist(i)
    else:
        xlist.append(a)

def addm(a,b,l):
    leng = len(a)
    x=[]

    #print(a,b)
    if l>2:
        #normalizing list
        xlist.clear()
        onedlist(a)
        a=xlist.copy()
        
        xlist.clear()
        onedlist(b)
        b=xlist.copy()

        #print(a,b)
        x=[]
        
    for i in range(0, len(a)):
        t=[]
        for j in range(0, len(a[i])):
            t.append(a[i][j]+b[i][j])
        x.append(t)
    return x

def dividematrix(a):
    leng = len(a)
    mid = int(leng/2)
    a11=[]
    a12=[]
    a21=[]
    a22=[]
    for i in range(0,mid):
        t=[]
        for j in range(0,mid):
            t.append(a[i][j])
        a11.append(t)

        tt=[]
        for j in range(mid, leng):
            tt.append(a[i][j])
        a12.append(tt)

    for i in range(mid, leng):
        t=[]
        for j in range(0,mid):
            t.append(a[i][j])
        a21.append(t)

        tt=[]
        for j in range(mid, leng):
            tt.append(a[i][j])
        a22.append(tt)

    if len(a11[0])<=1:
        n=[[a11[0][0],a12[0][0]],[a21[0][0],a22[0][0]]]
    else:
        n=[[a11,a12],[a21,a22]]

    #print("div fun",n)
    return n

#def multiplymatrix(a,b,ax1,ax2,ay1,ay2,bx1,bx2,by1,by2):
def multiplymatrix(a,b, l):
    
    alla = dividematrix(a)
    allb = dividematrix(b)
    if l > 2:

        #a
        a11=alla[0][0]
        a12=alla[0][1]
        a21=alla[1][0]
        a22=alla[1][1]
        #b
        b11=allb[0][0]
        b12=allb[0][1]
        b21=allb[1][0]
        b22=allb[1][1]

        ae=multiplymatrix(a11,b11,l/2)
        bg=multiplymatrix(a12,b21,l/2)
        af=multiplymatrix(a11,b12,l/2)
        bh=multiplymatrix(a12,b22,l/2)
        ce=multiplymatrix(a21,b11,l/2)
        dg=multiplymatrix(a22,b21,l/2)
        cf=multiplymatrix(a21,b12,l/2)
        dh=multiplymatrix(a22,b22,l/2)



        c11 =addm(multiplymatrix(a11,b11,l/2), multiplymatrix(a12,b21,l/2),l/2)
        c12 =addm(multiplymatrix(a11,b12,l/2), multiplymatrix(a12,b22,l/2),l/2)
        c21 =addm(multiplymatrix(a21,b11,l/2), multiplymatrix(a22,b21,l/2),l/2)
        c22 =addm(multiplymatrix(a21,b12,l/2), multiplymatrix(a22,b22,l/2),l/2)

        t=[[c11,c12],[c21,c22]]
        return t
        
    else:
        """
        print(a,"-",b)
        print("Star" ,strassens(a,b))
        print("-------")
        """
        return strassens(a,b)
    
    
def strassens(a, b):
    P=(a[0][0]+a[1][1])*(b[0][0]+b[1][1])
    Q=(a[1][0]+a[1][1])*b[0][0]
    R=a[0][0]*(b[0][1]-b[1][1])
    S=a[1][1]*(b[1][0]-b[0][0])
    T=(a[0][0]+a[0][1])*b[1][1]
    U=(a[1][0]-a[0][0])*(b[0][0]+b[0][1])
    V=(a[0][1]-a[1][1])*(b[1][0]+b[1][1])
    x=[[0,0],[0,0]]
    x[0][0]=P+S-T+V
    x[0][1]=R+T
    x[1][0]=Q+S
    x[1][1]=P+R-Q+U

    return x




s = int(input("Enter Matrix size : "))
tarr1=[]
print("Enter First Matrix")
for i in range(0,s):
    a=list(map(int, input().split()))
    tarr1.append(a)

tarr2=[]
print("Enter Second Matrix")
for i in range(0,s):
    a=list(map(int, input().split()))
    tarr2.append(a)
 

size=s
if math.log(s,2)-int(math.log(s,2))!=0.0 and s>2:
    size = 2**(int(math.log(s,2))+1)

arr1=[]
arr2=[]
arr3=[]
for i in range(0,size):
    l1=[]
    l2=[]
    l3=[]
    for j in range(0,size):
        l1.append(0)
        l2.append(0)
        l3.append(0)
        
    arr1.append(l1)
    arr2.append(l2)
    arr3.append(l3)

for i in range(0,len(tarr1)):
    for j  in range(0,len(tarr2)):
        arr1[i][j]=tarr1[i][j]
        arr2[i][j]=tarr2[i][j]

x = multiplymatrix(arr1,arr2,size)
"""
print("Divide and Conquer -- ")
for r in x:
   print(r)
"""

tarr3=[]
for i in range(0,s):
    ll=[]
    for j in range(0,s):
        ll.append(0)
    tarr3.append(ll)


# iterate through rows of X
for i in range(s):
   # iterate through columns of Y
   for j in range(s):
       # iterate through rows of Y
       for k in range(s):
           tarr3[i][j] += tarr1[i][k] * tarr2[k][j]

#print("Verify -- ")
for r in tarr3:
   print(r)

#onedlist(x)
#print(len(xlist))





#mul4(arr1, arr2)
#multiplymatrix(arr1,arr2,0, len(arr1),0, len(arr1),0,len(arr2),0,len(arr2))
#arr3 = strassens(arr1, arr2)

#printarr(arr3)
