#input
print("Enter Value of money : ")
coins = list(map(int, input().split()))
coins.sort()
amount = int(input("Enter the amount : "))

def greedycoin(c, amt):
    final = []
    a = amount
    while a>0:
        if len(coins)==0:
            print("Transaction not Possible")
            break

        m = coins.pop()
        if a>=m:
            num = int(a/m)
            final.append([m,num])
            a=a%m

    return final

#call
f=greedycoin(coins, amount)

#display
tc=0
for i in f:
    print(i[0]," x ",i[1]," = ", int(i[0]*i[1]))
    tc+=i[1]

print("Total Coins : ",tc)

