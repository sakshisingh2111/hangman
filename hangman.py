import random
from words import words

lives = 6
word_chosen = random.choice(words)
display = ['_'] * len(word_chosen)  
guessed_list=' '
print(display)

while lives > 0  and '_' in display:
    guessed_letter = input("Guess a letter: ")
    
    


    if len(guessed_letter) != 1 :
        print("Input a single letter")
        continue

    if guessed_letter in guessed_list:
        print("already guessed this alphabet")
        continue     


    if guessed_letter in word_chosen:
        
        for i in range(len(word_chosen)):
            letter = word_chosen[i]
            if letter == guessed_letter:
                display[i] = guessed_letter

     

    else:
        lives -= 1
            # print(lives)



    print(' '.join(display))   
    print("lives lft: ",lives)

    guessed_list += guessed_letter



if '_' not in display:
    print("Congratulations! You guessed the word:", word_chosen)
else:
    print("Game over. The word was:", word_chosen)         
