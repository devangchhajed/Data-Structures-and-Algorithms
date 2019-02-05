str1 = input("Enter 1st string : ")
str2 = input("Enter 2nd string : ")

matrix = []
for i in range(len(str2)+1):
    tt=[]
    for j in range(len(str1)+1):
        t=[]
        if i==0 or j==0:
            t.append(0)
            t.append([0,0,0])
        else:
            t.append(-1)
            t.append([0,0,0])
        tt.append(t)
    matrix.append(tt)


def populatematrix(s1, s2):
    for i in range(1,len(s2)+1):
        for j in range(1,len(s1)+1):
            
            back = matrix[i][j-1][0]
            diag = matrix[i-1][j-1][0]
            up = matrix[i-1][j][0]
            if s2[i-1]==s1[j-1]:
                diag=diag+1

            pos=[back,diag,up]
            maxval = max(pos)
            for mi in range(3):
                if maxval==pos[mi]:                    
                    matrix[i][j][1][mi]=1
                if s2[i-1]==s1[j-1]:
                    matrix[i][j][1][1]=0

            matrix[i][j][0]=maxval
            if s2[i-1]==s1[j-1]:
                diag=diag+1


path=[]
def nbconesol():
    i=len(str2)
    print("")
    print("BackTrack Coordinates : ")
    for j in range(len(str1),0,-1):
        if matrix[i][j][1][1]==1:
            print(i,",",j)
            path.append(str1[j-1])
            i-=1
        if matrix[i][j][1][2]==1:
            i-=1
            j+=1

    print("")
    print("LCS : ",end="")            
    path.reverse()
    for i in path:
        print(i, end="")



def printm():
    print("Table : ")
    print("", end ="\t")
    for i in range(len(str1)+1):
        if i==0:
            print(i, end ="\t")
        else:
            print(i,"-",str1[i-1], end ="\t")
    print("")
    for i in range(len(str1)+2):
        print("-------", end ="\t")
    print("")
    for i in range(len(str2)+1):
        if i==0:
            print(i, end ="\t|")
        else:
            print(i,"-",str2[i-1], end ="\t|")
        for j in range(len(str1)+1):
            print(matrix[i][j][0], end ="\t")
        print("")



populatematrix(str1, str2)
printm()
nbconesol()


