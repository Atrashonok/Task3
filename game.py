import click
import sys
import secrets
import math

numberOfArguments = len(sys.argv)
gameSize = int((numberOfArguments-1) / 2)

if numberOfArguments == 1:
    print("дядя, ты не передал аргументы")
    sys.exit(1)
elif numberOfArguments <= 3:
    print("слишком мало аргументов(должно быть не менее трех)")
    sys.exit(1)
elif numberOfArguments % 2 != 0:
    print("неверное количество аргументов(должно быть нечетное количество)")
    sys.exit(1)


secretsGenerator = secrets.SystemRandom()
computerChoice = secretsGenerator.randint(1,len(sys.argv)-1)

print("ход компьютера:", computerChoice)

print("it's your turn to choose: ")
for i in range(1, len(sys.argv)):
    print(i, ":  ", sys.argv[i])
print ("0", ":  ", "---EXIT---")

userChoice = int(input())

if userChoice == 0:
    print("-------Спасибо за игру, дай тебе бог здоровья-------")
    sys.exit()
elif (userChoice == computerChoice):
    print("НИЧЬЯ")
    sys.exit()
else:  
    controlVariable = userChoice - computerChoice

if controlVariable < 0:
    if math.fabs(controlVariable) <= gameSize:
        print("КРАСАВА, ТЫ ПОБЕДИЛ")
        sys.exit()
    else:
         print("ТЫ ПРОИГРАЛ")
         sys.exit()
elif controlVariable > 0:
    if (numberOfArguments-1) - controlVariable <= gameSize:
        print("КРАСАВА, ТЫ ПОБЕДИЛ")
        sys.exit()
    else:
        print("ТЫ ПРОИГРАЛ")
        sys.exit()
        

    