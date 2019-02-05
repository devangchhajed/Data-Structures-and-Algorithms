totalnodes = 0
totalcolors = 0
graph=[]
colorlist=[]
nodecolor=[]
solution=[]
def initgraph():
#    totalnodes=int(input("Total Nodes : "))
#    totalcolors=int(input("Total Colors : "))
    for i in range(0, totalnodes):
        a=set()
        graph.append(a)
        nodecolor.append(-1)

    for i in range(0, totalcolors):
        c = input("Enter colors : ")
        colorlist.append(c)
    

def enteredge():
    te = int(input("Enter total Edge : "))
    for i in range(0, te):
        n1, n2 = map(int,input().split())
        graph[n1].add(n2)
        graph[n2].add(n1)


def check(v, c):
    for i in graph[v]:
        if nodecolor[i]!=-1 and nodecolor[i]==c:
            return False

    return True
        
def sol(v):
    if v>totalnodes:
        return False
    if -1 not in nodecolor:
        return True

#    print("Starting loop for ",v)
    for colr in range(0, totalcolors):
#        print("check",v,colr)
        if check(v, colr):
            nodecolor[v] = colr
#            print(nodecolor)
            if sol(v+1)==True:
                if -1 not in nodecolor:
                    solution.append(nodecolor.copy())
                    nodecolor[v] = -1
                else:
                    return True
            else:
                nodecolor[v] = -1
#           print(nodecolor,"--")

    return False


def mainsol():
#    print(totalcolors)
    sol(0)
    print(len(solution), " solution found")
    for cl in solution:
        print("")
        print("colors : ",cl)
        for i in range(0,totalnodes):
            print("Node ",i," : ", colorlist[cl[i]])
        #print(nodecolor)
        
def printall():
    print(graph)
    print(colorlist)
    print(nodecolor)
    

totalnodes=int(input("Total Nodes : "))
totalcolors=int(input("Total Colors : "))

initgraph()
enteredge()
mainsol()
#printall()

    
        
