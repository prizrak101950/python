def calculatot():

    num1 = int(input("введите первое цисло"))
    num2 = int(input("введите второе число "))

    operation = input("введи операцию:" 
                      "+ для сложения \n"
                      "- для вычтания \n"
                      "* для умножения \n"
                      "/ для деления \n")
    if operation == "+":
        print("{} + {} = {}".format(num1, num2, num1 + num2))
    elif operation == "-":
        print("{} - {} = {}".format(num1, num2, num1 - num2))
    elif operation == "*":
        print("{} * {} = {}".format(num1, num2, num1 * num2))
    elif operation == "/":
        print("{} / {} = {}".format(num1, num2, num1 / num2))
    else:
        print("упс вы ввели что то не то")
calculatot()
