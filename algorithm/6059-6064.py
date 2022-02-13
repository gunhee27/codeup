#6059
a = int(input())
print((int(~a)))

#6060
a,b = input().split()
print(int(int(a) & int(b)))

#6061
a,b = input().split()
print(int(int(a) | int(b)))

#6062
a,b = input().split()
print(int(int(a) ^ int(b)))

#6063
x,y = input().split()
a = int(x)
b = int(y)
print(a if(a>=b) else b)

#6064
x,y,z = input().split()
a = int(x)
b = int(y)
c = int(z)
print((a if(a <= b) else b)if((a if(a <= b) else b)<c) else c)