s = input()
p = input()

q=[0]*(len(p)+1)


i=0

z = set(p)
z=list(z)
z.sort()
for i in range(0,len(q)-1):
    x=[]
    for j in range(0,len(z)):
        if p[i]==z[j]:
            x.append(i+1)
        else:
            ss = list(p[:i])
            ss.append(z[j])
            l1=ss[:-1]
            l2=ss[1:]
            while len(l1)>0 and len(l2)>0:
                if l1==l2:
                    break
                l1.pop()
                del(l2[0])
            
            x.append(len(l1))

    q[i]=x

q[-1]=[0]*len(z)
print("Q=",end="")
for i in range(len(q)):
    print(i, end=", ")

print("")
print("z=",set(z))
print('q0=0')
print("F=",len(q)-1)


for i in z:
    print("\t",i,end="")
print()
for i in range(len(q)):
    print(i,end="\t")
    for j in q[i]:
        print(j,end="\t")
    if i < len(q)-1:
        print(p[i],end="")
    print()


def checkSub(pp):
    st = s[pp:pp+len(p)]
    if st==p:
        return True
    else:
        False


pos=0
c=0
for i in range(len(s)):
    if s[i] in z:
        zz = z.index(s[i])
        pos = q[pos][zz]
        if pos==len(p):
            c+=1
            pos=0
            print("position", i+1-len(p))
    else:
        pos=0

print("Total Substring :",c)
