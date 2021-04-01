a = int(input("введи первое число"))
b = int(input("введи второе число"))
c = int(input("введи третье число"))

m = a
if(a < b) and (a < c):
    m = a
elif b < c:
    m = b
else:
    m = c
print(m)

d = int(input("введи  число"))
if d < 0:
    print(-1)
if d > 0:
    print(1)
