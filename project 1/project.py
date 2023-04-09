'''designed by Raisun Lakra'''
'''       T I T L E     :     W O R D    P U Z Z L E         '''

import random
from time import sleep
# we can import re(regular expression) module to search pattern ie is user word is present in wordList or not
# from re import search
# import sys

paragraph="""Books are wonderful companions. Books belong to various genres, and therefore we have a wide spectrum to choose from to read and enjoy and understand. They can take us on voyages to unexplored areas of the world as also of the mind and the spirit. They can take us back in time through historical material or into the future through science fiction. They can be in as many languages as there are in this world. They may be fictional stories or belong to the category of non-fiction. There could be horror, thriller, detective, romance or comedy stories in works of fiction. And likewise non-fiction books could be in the self-help, religion, spirituality, environment, cookery, travel and academic categories.

I love to read works of fiction in the English language. I enjoy reading leisurely. I fancy buying brand new books from book stores. I keep my books neat and clean, without dog-earing or marking on the pages. I have kept safely my collection of books. I now like reading books on kindle too. The latest book that I have read is titled The Picture of Dorian Gray by British writer, Oscar Wilde. The book, published more than a hundred and twenty years ago, still makes for good reading. The storyline is also not restricted by geographical boundaries. Set in England, it is relevant to anyone living in any part of the world. While it is a horror story, there are many lessons to learn about life and the mystery of Time and its passage. The book takes us through the life of a youth named Dorian Gray. Intoxicated by the beauty of his youth, he seeks for its permanence and a life of indulgence.

As he grows, he goes from bad to worse, treading recklessly and wants only on the path of sin and corruption, spoiling others too in the process, till he is saturated with the burden of his sins including that of committing murder. So as time moves inexorably, his desire for everlasting youth becomes his very retribution. The story points to how we can and should use our productive years of youth, and not waste and abuse the period of our life. For, time and tide wait for none, and time lost can never come back. I am very fascinated by the idea of Time, and this book delves into this issue through the story of a young man.

——– Written by N. KALYANI"""
# print("Read the given paragraph.\n")
# print(paragraph)
# print()
# not the best solution as i can still contain duplicate elements if it found two word ending with s or es or , as striping will happpen after checking the paragraph word is in the wordlist or not
# wordList=[word.rstip(',').rstrip('es').rstip('s') for word in paragraph.split() if word not in "aAiI" and word!='---' and word not in wordList]  

wordList=[word.rstrip(',').rstrip('es').rstrip('s').upper() for word in paragraph.split()]
wordList=list(set(wordList))

wordList.extend(['FATHER','MOTHER','SISTER','BROTHER','COUSIN','DOCTOR','NURSE','EMPLOYEE','MANAGER','TIE','AND','OR','IN','BAG','SHOE','BAG','SAND','SALARY','ENGINEER','BREAKFAST','DINNER','EAT','COFFEE','BITE','ARRANGE','APPLE','ORANGE','BALLOON','SOUND','VOICE','FROG','CAT','HELP','DANCE'])

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
        print(len(shuffled_word))

        # get user input and convert it to uppercase
        word=input("Form valid word : ").upper()

        # check if user input matches the word
        if word in wordList:
            print("correct")
            score+=1
        else:
            print("Wrong. The correct word is",word)

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