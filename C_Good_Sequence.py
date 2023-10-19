s=int(input())
arr = list(map(int, input().split()))
arr2={}
rmv=0

for i in arr:
    if i in arr2:
        arr2[i] += 1
    else:
        arr2[i] = 1


for i,n in arr2.items():
    # print(n,i)
    if(n>i):
        rmv+= n-i
    elif n<i:
        rmv+=n
print(rmv)
