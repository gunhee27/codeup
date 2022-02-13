#6065
a,b,c = input().split()
x = int(a)
y = int(b)
z = int(c)
if(x % 2 == 0): print(x)
if(y % 2 == 0): print(y)
if(z % 2 == 0): print(z)

#6066
a,b,c = input().split()
x = int(a)
y = int(b)
z = int(c)
if(x % 2 == 0): print("even") 
else: print("odd")
if(y % 2 == 0): print("even") 
else: print("odd")
if(z % 2 == 0): print("even") 
else: print("odd")

#6067
a = int(input())
if a < 0:
  if(a % 2 == 0): print("A")
  else: print("B")
else:
  if(a % 2 == 0):print("C")
  else: print("D")

#6068
a = int(input())
if a >= 90: print("A")
elif a >= 70: print("B")
elif a >= 40: print("C")
else: print("D")

#6069
a = input()
if a == "A" : print("best!!!")
elif a == "B" : print("good!!")
elif a == "C" : print("run!")
elif a == "D" : print("slowly~")
else : print("what?")

#6070
a = int(input())
if a // 3 == 1 : print("spring")
elif a // 3 == 2 : print("summer")
elif a // 3 == 3 : print("fall")
else : print("winter")