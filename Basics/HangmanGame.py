# Guess the number game.
import random
import time

HANGMANPICS = [
'''
  +---+
  |   |
      |
      |
      |
      |\\
========''','''
  +---+
  |   |
  0   |
      |
      |
      |\\
========''','''
  +---+
  |   |
  0   |
  |   |
      |
      |\\
========''','''
  +---+
  |   |
  0   |
 /|   |
      |
      |\\
========''','''
  +---+
  |   |
  0   |
 /|\\  |
      |
      |\\
========''','''
  +---+
  |   |
  0   |
 /|\\  |
 /    |
      |\\
========''','''
  +---+
  |   |
  0   |
 /|\\  |
 / \\  |
      |\\
========'''
    ]

MyDictionary = 'eat sleep drink hello wow cool slow glow'.split(); 
strSecret = ''
strGuessed = []
iFailedAttempts = 0

def DisplayHangman(iPic, strAns, strLetter=''):
    global strGuessed
    print(HANGMANPICS[iPic])
    print('-------------------')
    iAnsLen = len(strAns)
    if strLetter=='':
        strGuessed = ['_ ']*iAnsLen

    if strLetter in strAns:
        for i in range(len(strAns)):
            if strLetter == strAns[i]:
                strGuessed[i] = strLetter
    print('Your guess:- '+ ' '.join(strGuessed))
    print('Ans is '+strAns)

def ChooseNewWord():
    return MyDictionary[random.randint(0, len(MyDictionary)-1)]

def GuessLetter():
    print('Enter letter to continue...')
    bValidIn=False
    strLetter=''
    while bValidIn==False:
        strLetter = input()
        if len(strLetter) > 1:
            print('Single characters are supported')
        elif strLetter not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter valid letter.')
        else:
            bValidIn=True
    return strLetter

def GameOver(bWin=False):
    if bWin:
        print('Congratulations!!!')
    else:
        print('Better luck next time...')
    print('Do you want to play again? (yes or no)')
    strChoice = input()
    if strChoice == 'yes':
        StartGame()

def NextTurn():
    global iFailedAttempts
    strLetter = GuessLetter()
    if strLetter not in strSecret:
        iFailedAttempts +=1
    DisplayHangman(iFailedAttempts, strSecret, strLetter)
    
    if ''.join(strGuessed) == strSecret:
        GameOver(True)
    elif iFailedAttempts == len(HANGMANPICS)-1:
        GameOver(False)
    else:
        NextTurn();


def StartGame():
    global strSecret 
    strSecret = ChooseNewWord()
    DisplayHangman(0, strSecret)
    NextTurn();
    
StartGame()
