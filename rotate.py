arr = list(map(int,input("Enter array: ").split()))
s = int(input())
n = len(arr)
r =[0]*n
r1 = s%n
for i in range(n):
    index = (i+r1)%n
    r[index]
print(r)