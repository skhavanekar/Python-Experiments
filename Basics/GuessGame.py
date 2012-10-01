# Guess the number game.
import random

print('Hello World!!!')
print("What's your name?")
strName=input()
print('Welcome to the new world, '+strName)
print("Let's play a game, "+strName)
print('You will have to guess a number between 1 to 20 in 6 attempts')

iAttempts = 0
iAns = random.randint(1,20)
bResult = False

while iAttempts < 6:
    print('Guess now!!!')
    iAttempts +=1
    iGuess = int(input());
    if iGuess == iAns:
        bResult = True
        break
    elif iGuess < iAns:
        print('Guess too low!')
    else:
        print('Guess too high!')

if not bResult:
    print('Ans was '+str(iAns)+'. Better luck next time, '+strName+'!')
else:
    print('Good job '+ strName+'! You are great :) You guessed my number in '+ str(iAttempts)+' attempts.')
