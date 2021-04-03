a = int(input("введи первое число"))
b = int(input("введи второе число"))
c = int(input("введи третье число"))

mini = a
if(a < b) and (a < c):
    mini = a
elif b < c:
    mini = b
else:
    mini = c
print(mini)

d = int(input("введи  число"))
if d < 0:
    print(-1)
elif d > 0:
    print(1)
else:
    print(0)

