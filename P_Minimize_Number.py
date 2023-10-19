n=int(input())
arr= list(map(int, input().split()))
flag=False
# check
count=0

while(flag != True):
    for a in arr:
        if(a%2 != 0):
            flag=True
    if(flag != True):
        arr = list(map(lambda x: x//2, arr))
        count+=1

if count!=0:
    print(count)
else:
    print(0)