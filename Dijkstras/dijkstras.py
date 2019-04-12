import math


totalnodes = 0
graph=[]
path=[]
cost=[]
end=0





def printAll():
    print()
    print()
    print("Distance from",start,"to",end,"is", cost[end])
    print()
    print('vertex\tDistance from',start)
    for i in range(0,totalnodes):
        print(i,"\t",cost[i])
    print()


    path.reverse()
    print("Shortest Path")
    for i in range(1,len(path)):
        print(path[i-1][0],'-',path[i][0],'=',path[i][1])
    print(path[-1][0],'-',end,'=',cost[end])



def dij(src):
    for i in range(len(graph[src])):
        if graph[src][i]!=0:
            #print(cost[src],graph[src][i],cost[i])
            if cost[src]+graph[src][i]<cost[i]:
                cost[i]=cost[src]+graph[src][i]
                dij(i)

def findpath(src):
    for i in range(len(graph[src])):
        if graph[i][src]!=0:
            #print(cost[src],graph[src][i],cost[i])
            """
            if cost[i]+graph[i][src]=cost[src]:
                path.append(i, cost[i]+graph[i][src])
                dij(i)
            """
            if cost[src]-graph[i][src]==cost[i]:
                path.append([i, cost[src]-graph[i][src]])
                findpath(i)
                


#initialize all the variables
totalnodes=int(input("Total Nodes : "))
for i in range(0, totalnodes):
    d=list(map(int, input().split()))
    graph.append(d)
    
cost=[float("inf")]*totalnodes

start = int(input("Starting Node : "))
end = int(input("Ending Node : "))

cost[start]=0


#Calculate Minimum Cost between Start and End
dij(start)

#Find Shortest Path
findpath(end)

#Print Output
printAll()

