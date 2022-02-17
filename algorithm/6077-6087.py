#6077
a=int(input())
s = 0
for i in range(1, a+1):
  if( i % 2 == 0) : s = s + i
print(s)

#6078
a = input()
print(a)
while (a != 'q') :
  a = input()
  print(a)

#6079
a = int(input())
s = 0
i = 0
while(s < a) :
  i += 1
  s += i
print(i)

#6080
n,m = input().split()
a = int(n)
b = int(m)
for i in range(1, a+1):
  for j in range(1, b+1):
    print(i,j)

#6081
x = int(input(),16)
for i in range(1, 16):
  print('%X'%x,'*%X'%i,'=%X'%(x*i),sep='')

#6082
a = int(input())
for i in range(1, a+1):
  if (i % 10 == 3): print("X", end=' ')
  elif (i % 10 == 6): print("X", end=' ')
  elif (i % 10 == 9): print("X", end=' ')
  else : print(i, end=' ')

#6083
r,g,b = input().split()
for i in range(0, int(r)):
  for j in range(0,int(g)):
    for k in range(0,int(b)):
      print(i, j, k)
print(int(r)*int(g)*int(b))

#6084
h,b,c,s = input().split()
result = float(int(h) / 1024)*float(int(b) / 8) *int(c)*int(s)
print(format((result / 1024),"0.1f"),"MB")

#6085
w,h,b=input().split()
result = float(int(w) / 1024)*float(int(h) / 1024)*float(int(b)/8)
print(format(result, ".2f"),"MB")

#6086
a = int(input())
i = 1
s = 0
while (s < a):
  s += i
  i += 1
print(s)

#6087
a = int(input())
for i in range(1, a+1):
  if(i % 3 != 0): print(i)
