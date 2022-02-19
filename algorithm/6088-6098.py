#6088
a,d,n = input().split()
start = int(a)
for i in range(2,int(n) + 1):
  start = int(d) + start
print(start)

#6089
a,r,n = input().split()
start = int(a)
for i in range(2,int(n) + 1):
  start = int(r)*start
print(start)

#6090
a,m,d,n = input().split()
start = int(a)
mp = int(m)
dp = int(d)
np = int(n)
for i in range(2,np+1):
  start *= mp
  start += dp
print(start)

#6091
a,b,c = input().split()
d = 1
while(d%int(a) != 0 or d%int(b) != 0 or d%int(c) != 0):
  d += 1
print(d)

#6092
n=int(input())
a=input().split()
for i in range(n):
  a[i] = int(a[i])
d = []
for i in range(24):
  d.append(0)
for i in range(n):
  d[a[i]] += 1
for i in range(1,24):
  print(d[i],sep='')

#6093
n = int(input())
a = input().split()
d =[]
for i in range(n):
  d.append(a[n - 1 - i])
for i in range(n):
  print(d[i],sep='')

#6094
n = int(input())
a = input().split()
for i in range(n):
  a[i] = int(a[i])
a.sort()
print(a[0])

#6095
n = int(input())
d = []
for i in range(20):
  d.append([])
  for j in range(20):
    d[i].append(0)
for i in range(n):
  x,y = input().split()
  x = int(x)
  y = int(y)
  d[x][y] = 1
for i in range(1,20):
  for j in range(1,20):
    print(d[i][j],end=' ')
  print()

#6096
n = [[] * 19 for _ in range(19)]
for i in range(19):
    n[i] = list(map(int, input().split()))
a = int(input())
for i in range(a):
    x, y = map(int, input().split())
    for j in range(19):
        if (n[x - 1][j] == 0): n[x - 1][j] = 1
        elif (n[x - 1][j] == 1): n[x - 1][j] = 0
    for j in range(19):
        if (n[j][y - 1] == 0): n[j][y - 1] = 1
        elif (n[j][y - 1] == 1): n[j][y - 1] = 0
for i in range(19):
    for j in range(19):
        print(n[i][j], end=' ')
    print()


#6097
w,h = map(int, input().split())
arr = [[0] * h for _ in range(w)]
n = int(input())
for i in range(n):
  l,d,x,y = map(int,input().split())
  if d == 0:
    for j in range(y-1,y-1+l):
      if(j > h - 1): continue
      arr[x - 1][j] = 1
  else:
    for k in range(x-1,x-1+l):
      if(k > w - 1): continue
      arr[k][y - 1] = 1
for i in range(w):
  for j in range(h):
    print(arr[i][j],end=' ')
  print()

#6098
arr = [[] * 10 for _ in range(10)]
for i in range(10):
  arr[i] = list(map(int,input().split()))
x = 1
y = 1
while 1:
  if(arr[x][y] == 0): arr[x][y] = 9
  elif(arr[x][y] == 2):
    arr[x][y] = 9
    break
  if(arr[x][y + 1] == 1 and arr[x + 1][y] == 1):
    break
  if(arr[x][y + 1] != 1): y += 1
  elif(arr[x + 1][y] != 1): x += 1
for i in range(10):
  for j in range(10):
    print(arr[i][j],end=" ")
  print()