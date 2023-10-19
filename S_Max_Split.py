# s=input()
# l=0
# r=0
# count=0
# arr=list()

# for (i,c) in enumerate(s):
#     if(c=="L"):
#         l+=1
#         if(i+1<len(s)  and s[i+1]=="R" or i+1 == len(s) ):
#             x=0
#             count+=1
#             if(l<=r):
#                 arr.append(l)
#             else:
#                 arr.append(r)
#             print()
#             r=0
#             l=0
#     elif c=="R" :
#         r+=1
#         if(i+1<len(s)  and s[i+1]=="L" or i+1 == len(s)):
#             x=0
#             count+=1
#             if(l>=r):
#                 arr.append(l)
#             else:
#                 arr.append(r)
#             r=0
#             l=0

# print(count//2)
# for x in arr:
#     if x!=0:
#         for i in range(x):
#             print("L",end="")
#         for i in range(x):
#             print("R",end="")
#         print()


s = input()
count = 0
result = []

balance = 0
substring = ""

for c in s:
    substring += c
    if c == "L":
        balance += 1
    else:
        balance -= 1
    
    if balance == 0:
        count += 1
        result.append(substring)
        substring = ""

print(count)
for sub in result:
    print(sub)