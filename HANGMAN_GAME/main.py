import random
import hangman_words
import hangman_art

word_list = ['ardvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)
lives = 6

display = ['_'] * len(chosen_word)



print("Welcome to Hangman!")
print(hangman_art[lives])

while True:
    guess = input('Choose a random letter: ').lower()

    # Keep track if any blanks remain
    condn = False

    correct_guess = False

    for index, letter in enumerate(chosen_word):
        if guess == letter:
            display[index] = guess
            correct_guess = True
    
    if not correct_guess:
        lives -= 1

    print(' '.join(display))
    print(hangman_art[lives])

    # Check if any blanks remain
    if '_' not in display:
        print("Congratulations! You guessed the word:", chosen_word)
        break
    elif lives == 0:
        print("Sorry, you were not able to guess the word.")
        break
