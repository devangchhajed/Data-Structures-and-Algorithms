totalnodes = 0
graph=[]
visited=[]
solution=[]
def initgraph():
    for i in range(0, totalnodes):
        a=set()
        graph.append(a)
        visited.append(0)

stack=[]



def enteredge():
    te = int(input("Enter total Edge : "))
    for i in range(0, te):
        n1, n2 = map(int,input().split())
        graph[n1].add(n2)
        graph[n2].add(n1)


def isvisited(v):
    if visited[v]==0:
        return False
    return True
        
def sol(v, visited):
    if v>totalnodes:
        return False
    if 0 not in visited:
        if 0 in graph[v]:
            solution.append(stack)
            return True
        return False

    for i in graph[v]:
        if isvisited(i)==True:
            return False
        else:
            visited[i]=1
            if sol(i,visited)==True:
                print(i)
                stack.append(i)
                if 0 not in visited:
                    if 0 in graph[v]:
                        solution.append(stack)
                        return False
                return True
            else:
                visited[i]=0

    return False
        

    


def mainsol():
    if sol(0,visited)==False:
        print("Solution does not Exist")
        #print(nodecolor)
        
def printall():
    print(graph)
    print(colorlist)
    print(nodecolor)
    

totalnodes=int(input("Total Nodes : "))

initgraph()
enteredge()
mainsol()
#printall()

    
        
