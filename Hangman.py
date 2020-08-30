import random

words_list = ["python", "java", "kotlin", "javascript"]
print("H A N G M A N")

def hangman():
    chosen_word = random.choice(words_list)
    word = '-' * len(chosen_word)
    print(word)
    inputletters = set()
    answer = list(word)
    mistake = 0
    while mistake != 8:
        letter = input('Input a letter: ')
        if len(letter) == 0 or len(letter) > 1 :
            print("You should input a single letter")
        elif not letter.islower():
            print("It is not an ASCII lowercase letter")
        elif letter in inputletters and chosen_word:
            print('You already typed this letter')
        elif letter in chosen_word:
            for i in range(len(chosen_word)):
                if letter == chosen_word[i]:
                    answer[i] = letter
        else:
            print('No such letter in the word')
            mistake += 1
        if mistake < 8:
            print()
            print(''.join(answer))
        else:
            print('You are hanged!')
        if '-' not in answer:
            print('You survived!')
            break
        inputletters.add(letter)

while True:
    question = input('Type "play" to play the game, "exit" to quit: ')
    if question == "play":
        print()
        hangman()
        print()
    elif question == "exit":
        break