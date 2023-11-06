count = 0
n = int(input())
for i in range(1,n+1):
    z = i
    while z >0:
        if z % 10 == 1:
            count += 1
        z//=10
print(count)