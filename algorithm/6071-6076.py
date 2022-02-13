#6071
a = 1
while a != 0:
  a = int(input())
  if a != 0 : print(a)

#6072
a = int(input())
while a > 0 :
  print(a)
  a = a - 1

#6073
a = int(input())
while a >= 0 :
  a = a - 1
  if a >= 0 : print(a)

#6074
a = ord(input())
start = ord('a')
while start <= a :
  print(chr(start),end=' ')
  start += 1

#6075
a = int(input())
start = 0
while start <= a:
  print(start)
  start += 1

#6076
a = int(input())
for i in range(a + 1):
  print(i)