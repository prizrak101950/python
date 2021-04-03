count = 1
while count <= 3:

    a = int(input("введи первое число "))
    b = int(input("введи второе число "))
    c = int(input("введи третье число "))

    mx = a
    if (a > b) and (a > c):
        mx = a
    elif b > c:
        mx = b
    else:
        mx = c
    print(mx)
    count += 1
