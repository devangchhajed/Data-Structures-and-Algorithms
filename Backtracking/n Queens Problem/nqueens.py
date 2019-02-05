n = int(input("No. of Queens : "))
nb = int(input("Board : "))
queensposcol = [-1] * n
board = [ [0] * nb for _ in range(nb)]
sol=[]
def check(r,c):

    for i in range(nb):
        if board[i][c]==1 or board[r][i]==1:
            return False
    
    i=r+1
    j=c+1
    while i<nb and j<nb:
        if board[i][j]==1:
            return False
        i+=1
        j+=1

    i=r+1
    j=c-1
    while i<nb and j>=0:
        if board[i][j]==1:
            return False
        i+=1
        j-=1
        

    i=r-1
    j=c+1
    while i>=0 and j<nb:
        if board[i][j]==1:
            return False
        i-=1
        j+=1

        
    i=r-1
    j=c-1
    while i>=0 and j>=0:
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    
    return True



    
def nqueen(x):
    if x>=n:
        return True
    if -1 not in queensposcol:
        return True
    
    for i in range(nb):
        if check(x,i)==True:
            queensposcol[x]=i
            board[x][i]=1
            if nqueen(x+1)==True:
                if -1 not in queensposcol:
                    print("pos : ",queensposcol)
                    for ii in board:
                        print(ii)
                    print("")
                    sol.append(queensposcol.copy())
                    queensposcol[x]=-1
                    board[x][i]=0
                else:
                    return True
            else:
                queensposcol[x]=-1
                board[x][i]=0
                
    return False
            

def mainsol():
    nqueen(0)
    print(len(sol), " Solution found")

mainsol()
