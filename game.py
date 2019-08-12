import click
import sys
import secrets
import math
import hmac
import hashlib
import binascii
from termcolor import colored

CYELLOW = '\33[33m'
CEND = '\033[0m'

def create_sha256_signature(key, message):
    byte_key = binascii.unhexlify(key)
    message = message.encode()
    return hmac.new(byte_key, message, hashlib.sha256).hexdigest().upper()

def check():
    for i in range(1, len(sys.argv)):
        if i == computerChoice:
            print (CYELLOW,i, ": ", create_sha256_signature(str(preKey), str(i)), CEND)
        else:
            print (i, ": ", create_sha256_signature(str(preKey), str(i)))

            
numberOfArguments = len(sys.argv)
gameSize = int((numberOfArguments-1) / 2)

if numberOfArguments == 1:
    print("there are no arguments")
    sys.exit(1)
elif numberOfArguments <= 3:
    print("number of arguments is wrong(must be at least 3)")
    sys.exit(1)
elif numberOfArguments % 2 != 0:
    print("number of arguments is wrong(there must be an odd amount)")
    sys.exit(1)

secretsGenerator = secrets.SystemRandom()
computerChoice = secretsGenerator.randint(1,len(sys.argv)-1)

secretsGenerator = secrets.SystemRandom()
preKey = secretsGenerator.randint(11111111111111111111111111111111,99999999999999999999999999999999)

usedKey = create_sha256_signature(str(preKey), str(computerChoice))

print(CYELLOW, "KEY: ", usedKey, CEND)

print("it's your turn to choose: ")
for i in range(1, len(sys.argv)):
    print(i, ":  ", sys.argv[i])
print ("0:", "---EXIT---")

userChoice = int(input())

if userChoice == 0:
    print("-------thank yoyu, bye-------")
    sys.exit()
elif (userChoice == computerChoice):
    print("DRAW")
    check()
    sys.exit()
else:  
    controlVariable = userChoice - computerChoice

if controlVariable < 0:
    if math.fabs(controlVariable) <= gameSize:
        print("YOU WON")
        check()
        sys.exit()
    else:
         print("YOU LOSE")
         check()
         sys.exit()
elif controlVariable > 0:
    if (numberOfArguments-1) - controlVariable <= gameSize:
        print("YOU WON")
        check()
        sys.exit()
    else:
        print("YOU LOSE")
        check()
        sys.exit()
        