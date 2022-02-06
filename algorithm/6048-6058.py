#6048
a,b = input().split()
print(int(a) < int(b))

#6049
a,b = input().split()
print(int(a) == int(b))

#6050
a,b = input().split()
print(int(b) >= int(a))

#6051
a,b = input().split()
print(int(a) != int(b))

#6052
a = int(input())
print(bool(a))

#6053
a = bool(int(input()))
print(not a)

#6054
a,b = input().split()
print(bool(int(a)) and bool(int(b)))

#6055
a,b = input().split()
print(bool(int(a)) or bool(int(b)))

#6056
c,d = input().split()
a = bool(int(c))
b = bool(int(d))
print((a and (not b)) or (b and (not a)))

#6057
a,b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and d) or (not c and not d))

#6058
a,b = input().split()
c = bool(int(a))
d = bool(int(b))
print(not c and not d)