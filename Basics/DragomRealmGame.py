# Guess the number game.
import random
import time

def ShowIntro():
    print('In a Galaxy far far away...')
    time.sleep(2)
    print('There was a world full of dragons and mythical creatures...')
    time.sleep(2)
    print('A young warrior is on a journey of his lifetime in a search of this great treasure guarded by these dragons...')
    time.sleep(3)
    print('In front of you there are two caves. In one cave , the dragon is friendly and will share his treasure with you. The other dragon is greedy and hungry, and will eat you on the sight')
    time.sleep(3)
    print('\nMay the force be with you...\n\n')
    time.sleep(3)


def ChooseCave():
    ShowIntro()
    iGoodDragon = random.randint(1,2)
    print("Which cave will you go into? (1 or 2)")
    iCaveChoice=input()
    iCaveChoice = int(iCaveChoice)
    CaveEntryIntro(iCaveChoice == iGoodDragon)

    print('Do you want to play again? (yes or no)')
    strChoice = input()
    if strChoice == 'yes':
        ChooseCave()

def CaveEntryIntro(bGoodDragon=False):
    print('You approach the cave....')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens hi jaws and ...')
    time.sleep(2)
    if bGoodDragon:
        print('\nsays,"Welcome brave one. The force is strong in you. Take the treasure and use it for greater good."\n')
    else:
        print('\nGobbles you down in one bite!\n')


ChooseCave()
