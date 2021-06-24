import random, asc_art
from words import word_list
from os import system

system('cls || clear')

display_word = []
chosen_word = random.choice(word_list)
game_over = False
lifes = 6

# Adding underscores in which word letter
for letter in chosen_word:
    display_word += '_'


# -----------------------
# Some functions
# -----------------------

# Checks if the player chosen the right letter
def letterChecker():
    if guess in display_word:
        print(f'You already chosen {guess}!')
    else:
        for i in range(len(chosen_word)):
            letter = chosen_word[i] 
            if letter == guess:
                display_word[i] = letter 


# Checks if the player got all letters right
def winChecker():
    if '_' in display_word:
        return False
    return True


# Checks if the player chosen the wrong letter
def wrongGuessChecker():
    if guess not in chosen_word:
        print('You chosen a wrong letter. Losing 1 life')
        return True
    return False


# Game Loop
while not game_over:
    print(asc_art.stages[lifes])
    print(' '.join(display_word))
    guess = input('Guess a letter: ').lower()
    system('cls || clear')

    letterChecker()
    
    if winChecker():
        print(asc_art.stages[lifes])
        print(' '.join(display_word))
        print('You win!')
        game_over = True
    elif wrongGuessChecker():
        lifes -= 1

    if lifes <= 0:
        print(asc_art.stages[lifes])
        print(' '.join(display_word))
        print('You lose')
        game_over = True
