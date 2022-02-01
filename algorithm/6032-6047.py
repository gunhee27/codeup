#6032
a = input()
print(-int(a))

#6033
a = ord(input())
print(chr(a + 1))

#6034
a,b = input().split()
result = int(a) - int(b)
print(result)

#6035
a,b = input().split()
result = float(a) * float(b)
print(result)

#6036
w,n = input().split()
print(w * int(n))

#6037
n = input()
s = input()
print(s * int(n))

#6038
a, b = input().split()
print(int(a) ** int(b))

#6039
a, b = input().split()
print(float(a) ** float(b))

#6040
a, b = input().split()
print(int(a)//int(b))

#6041
a, b = input().split()
print(int(a)%int(b))

#6042
a = float(input())
print(format(a,".2f"))

#6043
a, b = input().split()
result = float(a) / float(b)
print(format(result,".3f"))

#6044
a, b = input().split()
print(int(a) + int(b))
print(int(a) - int(b))
print(int(a) * int(b))
print(int(a) // int(b))
print(int(a) % int(b))
print(format(float(a)/float(b),".2f"))

#6045
a, b, c = input().split()
sum = int(a) + int(b) + int(c)
avg = float(sum) / float(3)
print(sum, format(avg,".2f"))

#6046
a = int(input())
print(a << 1)

#6047
a, b = input().split()
print(int(a) << int(b))
