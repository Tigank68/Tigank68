import random 
import colorama 
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

def gamestart():

    word_list= ['dance','round','gamer','coder','money','place','medal','windy','fight','think','match','sandy']

    word_selection= word_list[random.randint(0, len(word_list)-1)]

    correct_place= False
    incorrect_place= False

    guesses=1

    while guesses!=6:
        user_guess= input('Enter guess {}: '.format(guesses))

        while len(user_guess) !=5:
            user_guess= input('You're guess must be five letters long.\nEnter guess {}: '.format(guesses))

        user_guess= user_guess.lower()

        corrected_word= ['','','','','']

        for i in range(0,len(user_guess)):
            correct_place= False
            incorrect_place= False
            for j in range(0,(len(word_selection))):
                if user_guess[i] == word_selection[j]:
                    if i==j:
                        corrected_word[i]= Back.GREEN+ user_guess[i]
                        correct_place= True
                    else:
                        if user_guess.count(user_guess[i])> 1:
                            incorrect_place= False
                        else:
                            incorrect_place= True
                            corrected_word[i]= (Back.YELLOW+ user_guess[i])

            if correct_place == False and incorrect_place == False:
                corrected_word[i]=(Back.RED+ user_guess[i])

        print(''.join(map(str, corrected_word)))
        print('\n')
        
        if user_guess== word_selection:
            print(Back.LIGHTGREEN_EX+ Fore.WHITE+ 'You Win!!')
            guesses=6
        else:
            guesses= guesses+1
            if guesses == 6:
                print('The word was:', word_selection)
                print(Back.LIGHTRED_EX+ Fore.WHITE+ 'You lose :((')
    

def menu():
    print(Fore.BLACK+ Style.BRIGHT + Back.MAGENTA + '\n\t\t\tWELCOME TO WORLDE')
    print(Fore.WHITE+ Style.DIM + Back.BLUE + '\nPress 1 to play\nPress 2 for the rules\nPress 3 to exit')

def rules():
    print(Fore.LIGHTMAGENTA_EX+ Style.BRIGHT + Back.BLACK+ '\n\t\t\tRULES OF WORDLE')
    print(Fore.WHITE+ Style.DIM + Back.BLUE + '\nA random word will be generate and you have FIVE chances to guess the word.\nIt will be revealed if each letter is in the correct place')
    print(Back.GREEN+ 'Letter is in the correct place')
    print(Back.YELLOW+ 'Letter is in the word but not in the correct place')
    print(Back.RED+ 'Letter is NOT in the word')
    exitbutton= ''
    while exitbutton != 0:
        exitbutton= int(input('Press 0 to exit: '))
    
    
    
    

menushow= True
while menushow== True:
    menu()
    choice= int(input())
    while choice > 3:
        choice= int(input('Please pick a valid option'))
    if choice == 1:
        gamestart()
    elif choice == 2:
        rules()
    else: 
        menu== False

