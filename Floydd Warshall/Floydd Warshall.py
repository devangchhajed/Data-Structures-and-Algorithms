import math


totalnodes = 0
graph=[]
path=[]
cost=[]
end=0
cost=[]





def fm():
    for k in range(totalnodes):
        for i in range(totalnodes):
            for j in range(totalnodes):
                cost[i][j] = min(cost[i][j] , cost[i][k]+ cost[k][j])
    for i in cost:
        for j in i:
            print(j, end='\t')
        print()


#initialize all the variables
totalnodes=int(input("Total Nodes : "))
for i in range(0, totalnodes):
    d=list(map(int, input().split()))
    for i in range(totalnodes):
        if d[i]==0:
            d[i]=float("inf")
    graph.append(d)

cost = graph.copy()

fm()



