import random
guessesTaken = 0
number = random.randint(1, 50)
print("привет,друг!как тебя зовут")
myName = input()
print("я готов,начнём!Скажи мне число от 1 до 50")
while guessesTaken < 6:
    print("как думаешь, что я загадал?")
    guess = input()
    guess = int(guess)
    guessesTaken += 1
    if guess < number:
        print("моё число больше")
    if guess > number:
        print("моё число меньше")
    if guess == number:
        guessesTaken = str(guessesTaken)
        print("Подравляю," + myName + "! ты выиграл испоьзовав всего " + guessesTaken + " попыток!")
        break
if guess != number:
    number = str(number)
    print("Извини, ты проиграл я загадал число" + number)
