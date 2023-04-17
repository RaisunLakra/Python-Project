'''designed by Raisun Lakra'''
'''       T I T L E     :     W O R D    P U Z Z L E         '''

import random
from time import sleep
from collections import Counter

wordList=['FATHER','MOTHER','SISTER','BROTHER','COUSIN','DOCTOR','NURSE','EMPLOYEE','MANAGER','TIE','AND','OR','IN','BAG','SHOE','BAG','SAND','SALLARY','ENGINEER','BREAKFAST','DINNER','EAT','COFFEE','BITE','ARRANGE','APPLE','ORANGE','BALLOON','SOUND','VOICE','FROG','CAT','HELP','DANCE','SILENT','LISTEN']

print("\n\n\n\t\t\t\t G\t A\t M\t E\n\t\t\t W   O   R   D      P   U   Z   Z   L   E\n\n")

while True:
    score=0
    selected_word = random.sample(wordList,5)

    for word in selected_word:

        print("\nArrange the word to form a valid word : ")
        
        # suffle the letters of the word
        shuffled_word=''.join(random.sample(word,len(word)))
        while shuffled_word==word:
            shuffled_word=''.join(random.sample(word,len(word)))
        
        print(shuffled_word)
        # print(len(shuffled_word))

        # get user input and convert it to uppercase
        user=input("Form valid word : ").upper()

        # check if user input matches the word
        if Counter(word)==Counter(user) and user in wordList:     # Counter constructor takes and iterable and return a dictionary like object which that maps each unique element in the iterable to its frequency count
            print("correct")
            score+=1
        else:
            print(f"Wrong. The correct word is {word}")


    print()
    if score==5:
        print("CONGRATS! you have passed all the test cases.")
    else:
        print("correct answers are : ")
        print(selected_word)    # correct answer

    print()
    print("Your total score is",score)
    print()

    # Decoration for winner
    if score==5:
        print("Hur_reh!!!!!.............")
        sleep(1)
        print("you are awesome")
        sleep(1)
        print("you are brilliant")
        sleep(1)

    # play again
    play=input("play again [Y/N] ").lower()
    if play=='y':
        continue
    else:
        exit()